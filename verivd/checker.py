#!/usr/bin/env python
# -*- coding: utf-8 -*-


from qgis.core import QgsWkbTypes, QgsSymbolLayer, QgsProperty
from verivd.spatialite import SpatialiteData, LayerInfo, SymbologyType


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
				symbology_properties={QgsSymbolLayer.PropertySize: QgsProperty.fromValue(5)}
			),
			LayerInfo(
				display_name='Checker - {} surface'.format(topic),
				layer_name='000_Checker_surface',
				sql_request=sql_request,
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='description',
				symbology_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
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
			if self.layer.geometryType() == QgsWkbTypes.PointGeometry:
				for symbol in self.layer.renderer().symbols():
					symbol.symbolLayer(0).setName(self.MARKER_SHAPE[i%(len(self.MARKER_SHAPE)-1)])  # TODO: check this
					i = i+1
			self.iface.layerTreeView().refreshLayerSymbology(self.layer.id())
