# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VeriVDDockWidget
                                 A QGIS plugin
 Vérification des mensurations vaudoises
                             -------------------
        begin                : 2022
        git sha              : $Format:%H$
        copyright            : (C) 2018 by FSN/OIT
        email                : fabien.simon@vd.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from enum import Enum
from datetime import date

from qgis.PyQt.QtCore import pyqtSignal, QObject

from qgis.core import Qgis, QgsFeatureRequest, QgsFeature, QgsProject, QgsWkbTypes, edit, QgsProviderRegistry, QgsProviderSublayerDetails

from verivd.core.plugin_info import dbg_info
from verivd.core.gpkg_data import GpkgData


class GeometryType(Enum):
    NO_GEOMETRY = "NO_GEOMETRY"
    POLYGON = "POLYGON"
    LINE = "LINE"
    POINT = "POINT"


class Justificatif(QObject):
    # progress:
    # 0-20: deleting former features (statut = nouveau)
    # 20-50: creating qgis layers
    # 50-80: finding justificatif in gpkg
    # 80-100: writing to layers
    progress_changed = pyqtSignal(int, str)

    def __init__(self, parent=None):
        self.canceled = False
        super(Justificatif, self).__init__(parent)

    def cancel(self):
        self.canceled = True

    def process_justificatif(self, gpkg_data: GpkgData):
        self.canceled = False
        progress = 0

        justificatif_layer_no_geometry = {
            "qgis_layer": None,
            "layer_name": "justificatif_nogeometry",
            "title": "justificatif - sans géométrie",
            "features": [],
            "geometry_type": GeometryType.NO_GEOMETRY,
        }
        justificatif_layer_point = {
            "qgis_layer": None,
            "layer_name": "justificatif_point",
            "title": "justificatif - point",
            "features": [],
            "geometry_type": GeometryType.POINT,
        }
        justificatif_layer_line = {
            "qgis_layer": None,
            "layer_name": "justificatif_line",
            "title": "justificatif - lignes",
            "features": [],
            "geometry_type": GeometryType.LINE,
        }
        justificatif_layer_polygon = {
            "qgis_layer": None,
            "layer_name": "justificatif_polygon",
            "title": "justificatif - polygones",
            "features": [],
            "geometry_type": GeometryType.POLYGON,
        }

        justificatif_layers = {
            QgsWkbTypes.NoGeometry: justificatif_layer_no_geometry,
            QgsWkbTypes.PointGeometry: justificatif_layer_point,
            QgsWkbTypes.LineGeometry: justificatif_layer_line,
            QgsWkbTypes.PolygonGeometry: justificatif_layer_polygon,
        }

        for jf in justificatif_layers.values():
            veri_vd_id = f'VERID_VD_{jf["geometry_type"].value}'
            for ql in QgsProject.instance().mapLayers().values():
                if ql.customProperty("verid_vd_id") == veri_vd_id:
                    jf["qgis_layer"] = ql
                    break
            if jf["qgis_layer"] is None:
                jf["qgis_layer"] = gpkg_data.create_qgis_layer(jf["title"], jf["layer_name"], custom_properties={"verid_vd_id": veri_vd_id})

        justificatif_qgis_layers = [jf["qgis_layer"] for jf in justificatif_layers.values()]
        QgsProject.instance().addMapLayers(justificatif_qgis_layers)

        # delete current justificatifs
        for layer in justificatif_qgis_layers:
            if self.canceled:
                return
            self.progress_changed.emit(int(progress), f"Suppression des justificatifs de la session dans la couche {layer.name()}")
            progress += 5

            req = QgsFeatureRequest()
            req.setFilterExpression("\"statut\" = 'nouveau'")
            features_to_delete = []
            for justif_feature in layer.getFeatures(req):
                features_to_delete.append(justif_feature.id())
            with edit(layer):
                layer.deleteFeatures(features_to_delete)

        layer_details = QgsProviderRegistry.instance().querySublayers(gpkg_data.path, Qgis.SublayerQueryFlag.ResolveGeometryType)
        layers = []
        for layer_detail in layer_details:
            if self.canceled:
                return
            progress += 1 / len(layer_details) * 30

            if layer_detail.name().startswith("justificatif"):
                continue

            self.progress_changed.emit(int(progress), f"Creation des couches: {layer_detail.name()}")

            dbg_info(f"getting layer {layer_detail.name()}")

            options = QgsProviderSublayerDetails.LayerOptions(QgsProject.instance().transformContext())
            options.loadDefaultStyle = False
            layer = layer_detail.toLayer(options)

            layers.append(layer)

        for layer in layers:
            if self.canceled:
                return
            progress += 1 / len(layers) * 30
            self.progress_changed.emit(int(progress), f"Recherche de justificatif dans {layer_detail.name()}")

            req = QgsFeatureRequest()
            req.setFilterExpression("\"justificatif\" != ''")

            for topic_feature in layer.getFeatures(req):
                dbg_info(f"layer {layer.name()}: found feature {topic_feature.id()}")
                geometry_type = topic_feature.geometry().type()
                justif_layer = justificatif_layers.get(geometry_type, justificatif_layer_no_geometry)

                justif_feature = QgsFeature(justif_layer["qgis_layer"].fields())
                justif_feature.setGeometry(topic_feature.geometry())
                justif_feature["layer"] = layer.name()
                if topic_feature.fields().indexFromName("topic") >= 0:
                    justif_feature["topic"] = topic_feature["topic"]
                else:
                    justif_feature["topic"] = ""
                justif_feature["session"] = date.today().isoformat()
                justif_feature["statut"] = "nouveau"
                justif_feature["texte"] = topic_feature["justificatif"]
                # justif_feature["operateur"] = ""

                justif_layer["features"].append(justif_feature)

        for layer in justificatif_layers.values():
            dbg_info(f"couche justificatif {layer['geometry_type'].value}: enregistrement de {len(layer['features'])} objets")
            if len(layer["features"]):
                self.progress_changed.emit(int(progress), f"Ecriture des justificatifs ({len(layer['features'])}) dans la couche {layer['layer_name']}")
                qgs_layer = layer["qgis_layer"]
                dbg_info(f"qgis layer valid: {qgs_layer.isValid()}")
                with edit(qgs_layer):
                    ok = qgs_layer.addFeatures(layer["features"])
                    dbg_info(f"features added: {ok}")
            progress += 5
            self.progress_changed.emit(100, None)
