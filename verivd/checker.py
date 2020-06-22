#!/usr/bin/env python
# -*- coding: utf-8 -*-


from qgis.core import QgsWkbTypes, QgsSymbolLayer, QgsProperty, QgsRenderContext, QgsExpressionContextUtils
from verivd.core.spatialite_data import SpatialiteData, MARKER_SHAPE
from verivd.core.symbolgy_type import SymbologyType
from verivd.core.layer_info import LayerInfo


class Checker(SpatialiteData):
	"""Class used to load checker's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)

	def load_layer(self, topic):
		sql_request = '"topic" = "{}"'.format(topic)
		self.group_name = "Résultat du checker - {}".format(topic)

		self.layer_infos = (
			LayerInfo(
				display_name='Checker - {} point'.format(topic),
				layer_name='000_Checker_point',
				sql_request=sql_request,
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='description',
				symbology_data_defined_properties={QgsSymbolLayer.PropertySize: QgsProperty.fromValue(5)}
			),
			LayerInfo(
				display_name='Checker - {} surface'.format(topic),
				layer_name='000_Checker_surface',
				sql_request=sql_request,
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='description',
				symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
				opacity=.5
			),
			LayerInfo(
				display_name='Checker - {} sans géométrie'.format(topic),
				layer_name='000_Checker_sans_geometrie',
				sql_request=sql_request,
				symbology_type=SymbologyType.NO_SYMBOL
			)
		)

		super(Checker, self).load_layer()

		for self.layer in self.layers:
			i = 0
			context = QgsRenderContext.fromMapSettings(self.iface.mapCanvas().mapSettings())
			context.expressionContext().appendScope(QgsExpressionContextUtils.layerScope(self.layer))
			if self.layer.geometryType() == QgsWkbTypes.PointGeometry:
				for symbol in self.layer.renderer().symbols(context):
					symbol.symbolLayer(0).setShape(MARKER_SHAPE[i%(len(MARKER_SHAPE)-1)])
					i = i+1
			self.iface.layerTreeView().refreshLayerSymbology(self.layer.id())
