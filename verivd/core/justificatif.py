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

from qgis.core import Qgis, QgsFeatureRequest, QgsFeature, QgsProject, QgsWkbTypes, edit, QgsProviderRegistry, QgsProviderSublayerDetails

from verivd.core.plugin_info import dbg_info
from verivd.core.gpkg_data import GpkgData


class GeometryType(Enum):
    NO_GEOMETRY = "NO_GEOMETRY"
    POLYGON = "POLYGON"
    LINE = "LINE"
    POINT = "POINT"


def process_justificatif(gpkg_data: GpkgData):

    justificatif_layer_no_geometry = {
        "layer": gpkg_data.create_layer("justificatif - sans géométrie", "justificatif", f"\"GEOMETRY_TYPE\" = '{GeometryType.NO_GEOMETRY.value}'"),
        "features": [],
        "geometry_type": GeometryType.NO_GEOMETRY,
    }
    justificatif_layer_point = {
        "layer": gpkg_data.create_layer("justificatif - point", "justificatif", f"\"GEOMETRY_TYPE\" = '{GeometryType.POINT.value}'"),
        "features": [],
        "geometry_type": GeometryType.POINT,
    }
    justificatif_layer_line = {
        "layer": gpkg_data.create_layer("justificatif - lignes", "justificatif", f"\"GEOMETRY_TYPE\" = '{GeometryType.LINE.value}'"),
        "features": [],
        "geometry_type": GeometryType.LINE,
    }
    justificatif_layer_polygon = {
        "layer": gpkg_data.create_layer("justificatif - polygones", "justificatif", f"\"GEOMETRY_TYPE\" = '{GeometryType.POLYGON.value}'"),
        "features": [],
        "geometry_type": GeometryType.POLYGON,
    }

    layers = [jf["layer"] for jf in [justificatif_layer_no_geometry, justificatif_layer_point, justificatif_layer_line, justificatif_layer_polygon]]
    QgsProject.instance().addMapLayers(layers)

    justificatif_layers = {
        QgsWkbTypes.PointGeometry: justificatif_layer_point,
        QgsWkbTypes.LineGeometry: justificatif_layer_line,
        QgsWkbTypes.PolygonGeometry: justificatif_layer_polygon,
    }

    layer_details = QgsProviderRegistry.instance().querySublayers(gpkg_data.path, Qgis.SublayerQueryFlag.ResolveGeometryType)
    layers = []
    for layer_detail in layer_details:
        dbg_info(f"processing layer: {layer_detail.name()}")

        if layer_detail.name() == "justificatif":
            continue

        options = QgsProviderSublayerDetails.LayerOptions(QgsProject.instance().transformContext())
        options.loadDefaultStyle = False
        layer = layer_detail.toLayer(options)

        layers.append(layer)

    layers = QgsProject.instance().addMapLayers(layers, False)

    for layer in layers:
        req = QgsFeatureRequest()
        req.setFilterExpression("\"justificatif\" != ''")

        for topic_feature in layer.getFeatures(req):
            dbg_info(f"found feature {topic_feature.id()}")
            geometry_type = topic_feature.geometry().type()
            justif_layer = justificatif_layers.get(geometry_type, justificatif_layer_no_geometry)

            justif_feature = QgsFeature(justif_layer["layer"].fields())
            justif_feature.setGeometry(topic_feature.geometry())
            justif_feature["topic"] = layer.name()
            justif_feature["geometry_type"] = justif_layer["geometry_type"]
            justif_feature["session"] = "XXX"
            justif_feature["statut"] = "nouveau"
            justif_feature["texte"] = topic_feature["justificatif"]
            justif_feature["operateur"] = "xxx"

            justif_layer["features"].append(justif_feature)

    for layer in justificatif_layers.values():
        dbg_info(f"couche justificatif {layer['geometry_type'].value}: enregistrement de {len(layer['features'])} objets")
        if len(layer["features"]):
            qgs_layer = layer["layer"]
            with edit(qgs_layer):
                qgs_layer.addFeatures(layer["features"])
            # QgsProject.instance().addMapLayer(qgs_layer)

    for layer in layers:
        QgsProject.instance().removeMapLayer(layer)
