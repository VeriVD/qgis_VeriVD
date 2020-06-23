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

from qgis.core import QgsSymbolLayer, QgsProperty, QgsVectorLayer, QgsWkbTypes, QgsRenderContext, QgsExpressionContextUtils
from qgis.gui import QgisInterface

from verivd.core.layer_info import LayerInfo
from verivd.core.layer_list_model import LayerListModel
from verivd.core.layer_names import DONNEES_TOPIC
from verivd.core.spatialite_data import MARKER_SHAPE
from verivd.core.symbolgy_type import SymbologyType
from verivd.core.veri_layer import VeriLayer


class CheckerLayerModel(LayerListModel):
    def __init__(self, iface: QgisInterface):
        super(CheckerLayerModel, self).__init__(iface)

    def reload(self):
        self._veri_layers = []
        if not self.spatialite_data:
            return
        checker_dict = self.spatialite_data.load_table_list('000_checker_decompte')
        for topic in DONNEES_TOPIC:
            if topic in checker_dict:
                display_name = 'Checker - {}: {}'.format(topic, str(checker_dict[topic]))
                self._veri_layers.append(VeriLayer(topic, display_name))

    def layer_infos(self, layer: str) -> [LayerInfo]:
        sql_request = '"topic" = "{}"'.format(layer)
        layer_infos = (
            LayerInfo(
                display_name='Checker - {} point'.format(layer),
                layer_name='000_Checker_point',
                sql_request=sql_request,
                symbology_type=SymbologyType.RANDOM_CATEGORIZED,
                category_field='description',
                symbology_data_defined_properties={QgsSymbolLayer.PropertySize: QgsProperty.fromValue(5)}
            ),
            LayerInfo(
                display_name='Checker - {} surface'.format(layer),
                layer_name='000_Checker_surface',
                sql_request=sql_request,
                symbology_type=SymbologyType.RANDOM_CATEGORIZED,
                category_field='description',
                symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
                opacity=.5
            ),
            LayerInfo(
                display_name='Checker - {} sans géométrie'.format(layer),
                layer_name='000_Checker_sans_geometrie',
                sql_request=sql_request,
                symbology_type=SymbologyType.NO_SYMBOL
            )
        )
        return layer_infos

    def post_process_layer(self, layer: QgsVectorLayer, position: int):
        context = QgsRenderContext.fromMapSettings(self.iface.mapCanvas().mapSettings())
        context.expressionContext().appendScope(QgsExpressionContextUtils.layerScope(layer))
        if layer.geometryType() == QgsWkbTypes.PointGeometry:
            for symbol in layer.renderer().symbols(context):
                symbol.symbolLayer(0).setShape(MARKER_SHAPE[position % (len(MARKER_SHAPE) - 1)])
