# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VeriVD plugin
 Copyright (C) 2019 Denis Rouzaud
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

from qgis.gui import QgisInterface
from qgis.core import QgsSymbolLayer, QgsProperty, QgsWkbTypes, QgsVectorLayer

from verivd.core.layer_info import LayerInfo
from verivd.core.layer_list_model import LayerListModel
from verivd.core.topic_layers import TOPIC_LAYERS
from verivd.core.gpkg_data import MARKER_SHAPE
from verivd.core.symbology_type import SymbologyType
from verivd.core.veri_meta_layer import VeriMetaLayer


class IliValidatorLayerModel(LayerListModel):
    def __init__(self, iface: QgisInterface):
        super(IliValidatorLayerModel, self).__init__(iface)

    def reload(self):
        self.beginResetModel()
        self._veri_meta_layers = []
        if not self.gpkg_data:
            return
        ili_validator_dict = self.gpkg_data.load_table_list("000_iliValidator_decompte")
        for topic in TOPIC_LAYERS:
            ili_validator_topic = topic.replace(" ", "_")
            if ili_validator_topic in list(ili_validator_dict.keys()):
                display_name = "IliValidator - {}: {}".format(topic, str(ili_validator_dict[ili_validator_topic]))
                ili_validator_topic = topic.replace(" ", "_")
                self._veri_meta_layers.append(VeriMetaLayer(ili_validator_topic, display_name))
        self.endResetModel()

    def group_name(self, layer):
        return "Résultat du iliValidator - {}".format(layer)

    def layer_infos(self, layer: str):
        sql_request = "\"topic\" = '{}'".format(layer)
        layer_infos = (
            LayerInfo(
                display_name="Justificatifs - {} point".format(layer),
                layer_name="justificatif_point",
                sql_request=f"\"layer\" = '000_ilivalidator_point' AND {sql_request}",
                symbology_type=SymbologyType.QML,
            ),
            LayerInfo(
                display_name="Justificatifs - {} ligne".format(layer),
                layer_name="justificatif_line",
                # les lignes sont dans la couche _surface
                sql_request=f"\"layer\" = '000_ilivalidator_surface' AND {sql_request}",
                symbology_type=SymbologyType.QML,
            ),
            LayerInfo(
                display_name="Justificatifs - {} surface".format(layer),
                layer_name="justificatif_polygon",
                sql_request=f"\"layer\" = '000_ilivalidator_surface' AND {sql_request}",
                symbology_type=SymbologyType.QML,
            ),
            LayerInfo(
                display_name="Justificatifs - {} sans géométrie".format(layer),
                layer_name="justificatif_nogeometry",
                sql_request=f"\"layer\" = '000_ilivalidator_sans_geometrie' AND {sql_request}",
                symbology_type=SymbologyType.NO_SYMBOL,
            ),
            LayerInfo(
                display_name="iliValidator - {} point".format(layer),
                layer_name="000_iliValidator_Point",
                symbology_type=SymbologyType.RANDOM_CATEGORIZED,
                category_field="observation",
                symbology_data_defined_properties={QgsSymbolLayer.PropertySize: QgsProperty.fromValue(5)},
                sql_request=sql_request,
            ),
            LayerInfo(
                display_name="iliValidator - {} ligne".format(layer),
                layer_name="000_iliValidator_Ligne",
                symbology_type=SymbologyType.RANDOM_CATEGORIZED,
                category_field="observation",
                symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
                sql_request=sql_request,
                opacity=0.5,
            ),
            LayerInfo(
                display_name="iliValidator - {} Arc".format(layer),
                layer_name="000_iliValidator_Point_Arc",
                symbology_type=SymbologyType.RANDOM_CATEGORIZED,
                category_field="observation",
                symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
                sql_request=sql_request,
                opacity=0.5,
            ),
            LayerInfo(
                display_name="iliValidator - {} surface".format(layer),
                layer_name="000_iliValidator_Surface",
                symbology_type=SymbologyType.RANDOM_CATEGORIZED,
                category_field="observation",
                symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
                sql_request=sql_request,
                opacity=0.5,
            ),
            LayerInfo(
                display_name="iliValidator - {} sans géométrie".format(layer),
                layer_name="000_iliValidator_Sans_geometrie",
                symbology_type=SymbologyType.NO_SYMBOL,
                sql_request=sql_request,
            ),
            LayerInfo(
                display_name="Périmetre du lot",
                layer_name="112_itf_mise_a_jourrp",
            ),
        )
        return layer_infos

    def post_process_layer(self, layer: QgsVectorLayer, position: int):
        if layer.geometryType() == QgsWkbTypes.PointGeometry:
            for symbol in layer.renderer().symbols(self.layer_context(layer)):
                symbol.symbolLayer(0).setShape(MARKER_SHAPE[position % (len(MARKER_SHAPE) - 1)])
