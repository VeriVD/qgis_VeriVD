#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .spatialite import SpatialiteData
from qgis.core import QgsWkbTypes, QgsSymbolLayer, QgsProperty


# display_name, layerName, sqlRequest, symb, trans, visib

class Checker(SpatialiteData):
	"""Class used to load checker's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)
		self.layers = []

	def load_layer(self, topic):
		self.topic = topic
		self.sqlRequest = '"topic" = "{}"'.format(self.topic)
		self.group_name = "Résultat du checker - {}".format(self.topic)
		self.markerShape = ('square', 'diamond', 'pentagon', 'triangle', 'equilateral_triangle', 'star', 'regular_star', 'arrow', 'circle', 'filled_arrowhead')

		self.layer_infos = (
			['Checker - {} point'.format(self.topic), "000_Checker_point", self.sqlRequest,['randomCategorized', {'field':u'description', QgsSymbolLayer.PropertySize: QgsProperty.fromValue(5)}], '', ''],
			['Checker - {} surface'.format(self.topic), "000_Checker_surface", self.sqlRequest,['randomCategorized', {'field':u'description', QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)}], 50, ''],
			['Checker - {} sans géométrie'.format(self.topic), "000_Checker_sans_geometrie", self.sqlRequest, ['NoGeom'], '', '']
		)

		super(Checker, self).load_layer()

		for self.layer in self.layers:
			i = 0
			if self.layer.geometryType() == QgsWkbTypes.PointGeometry:
				self.symbols = self.layer.renderer().symbols()
				for self.symbol in self.symbols:
					self.symbol.symbolLayer(0).setName(self.markerShape[i%(len(self.markerShape)-1)])
					i=i+1
			self.iface.layerTreeView().refreshLayerSymbology(self.layer.id())
