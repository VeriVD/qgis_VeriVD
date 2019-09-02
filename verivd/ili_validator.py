#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qgis.core import QgsWkbTypes, QgsSymbolLayer, QgsProperty
from verivd.spatialite import SpatialiteData, LayerInfo, SymbologyType, MARKER_SHAPE


class IliValidator(SpatialiteData):
	"""Class used to load iliValidator's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)

	def load_layer(self, topic):
		sql_request = '"topic" = "{}"'.format(topic)
		self.group_name = "Résultat du iliValidator - {}".format(topic)

		self.layer_infos = (
			LayerInfo(
				display_name='iliValidator - {} point'.format(topic),
				layer_name='000_ilivalidator_point',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='observation',
				symbology_data_defined_properties={QgsSymbolLayer.PropertySize: QgsProperty.fromValue(5)},
				sql_request=sql_request
			),
			LayerInfo(
				display_name='iliValidator - {} ligne'.format(topic),
				layer_name='000_ilivalidator_ligne',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='observation',
				symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
				sql_request=sql_request,
				opacity=.5
			),
			LayerInfo(
				display_name='iliValidator - {} Arc'.format(topic),
				layer_name='000_iliValidator_point_Arc',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='observation',
				symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
				sql_request=sql_request,
				opacity=.5
			),
			LayerInfo(
				display_name='iliValidator - {} surface'.format(topic),
				layer_name='000_ilivalidator_surface',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='observation',
				symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
				sql_request=sql_request,
				opacity=.5,
			),
			LayerInfo(
				display_name='iliValidator - {} sans géométrie'.format(topic),
				layer_name='000_ilivalidator_sans_geometrie',
				symbology_type=SymbologyType.NO_SYMBOL,
				sql_request=sql_request
			)
		)

		super(IliValidator,self).load_layer()

		for self.layer in self.layers:
			i = 0
			if self.layer.geometryType() == QgsWkbTypes.PointGeometry:
				for symbol in self.layer.renderer().symbols():
					symbol.symbolLayer(0).setName(MARKER_SHAPE[i % (len(MARKER_SHAPE)-1)])
					i = i+1
			self.iface.layerTreeView().refreshLayerSymbology(self.layer.id())
