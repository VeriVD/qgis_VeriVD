#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qgis.core import QgsWkbTypes, QgsSymbolLayer, QgsProperty

from verivd.spatialite import SpatialiteData, LayerInfo, SymbologyType


class IliValidator(SpatialiteData):
	"""Class used to load iliValidator's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)

	def load_layer(self, topic):
		sql_request = '"topic" = "'+ topic + '"'
		self.group_name = u"Résultat du iliValidator - " + topic
		self.markerShape = ('square', 'diamond', 'pentagon', 'triangle', 'equilateral_triangle', 'star', 'regular_star', 'arrow', 'circle', 'filled_arrowhead')

		self.layer_infos = (
			LayerInfo(
				display_name='iliValidator - {} point'.format(topic),
				layer_name='000_ilivalidator_point',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='observation',
				symbology_properties={QgsSymbolLayer.PropertySize: QgsProperty.fromValue(5)},
				sql_request=sql_request
			),
			LayerInfo(
				display_name='iliValidator - {} ligne'.format(topic),
				layer_name='000_ilivalidator_ligne',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='observation',
				symbology_properties={QgsSymbolLayer.Width: QgsProperty.fromValue(2)},
				sql_request=sql_request,
				opacity=.5
			),
			LayerInfo(
				display_name='iliValidator - {} surface'.format(topic),
				layer_name='000_iliValidator_point_Arc',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='observation',
				symbology_properties={QgsSymbolLayer.Width: QgsProperty.fromValue(2)},
				sql_request=sql_request,
				opacity=.5
			),
			LayerInfo(
				display_name='iliValidator - {} surface'.format(topic),
				layer_name='000_ilivalidator_surface',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='observation',
				symbology_properties={QgsSymbolLayer.StrokeWidth: QgsProperty.fromValue(2)},
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
				self.symbols = self.layer.renderer().symbols()
				for self.symbol in self.symbols:
					self.symbol.symbolLayer(0).setName(self.markerShape[i % (len(self.markerShape)-1)])  # TODO Check this with new API
					i = i+1
			self.iface.layerTreeView().refreshLayerSymbology(self.layer.id())
