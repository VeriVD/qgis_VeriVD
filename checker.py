#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Connection class import
from __future__ import absolute_import
from .spatialite import SpatialiteData

# # Custom imports
from random import randrange
from qgis.PyQt.QtWidgets import QMessageBox, QDialog

class Checker(SpatialiteData):
	"""Class used to load checker's layers"""
	def __init__(self,iface, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.iface = iface
		self.layers = []

	def load_layer(self, topic):
		self.topic = topic
		self.sqlRequest = '"topic" = "'+ self.topic + '"'
		self.groupName = u"Résultat du checker - " + self.topic
		self.markerShape = ('square', 'diamond', 'pentagon', 'triangle', 'equilateral_triangle', 'star', 'regular_star', 'arrow', 'circle', 'filled_arrowhead')

		self.infoLayer = 	(
							[u'Checker - ' + self.topic + u' point',"000_Checker_point", self.sqlRequest,['randomCategorized',{'field':u'description','size':'5'}],'',''], 
							[u'Checker - ' + self.topic + u' surface',"000_Checker_surface", self.sqlRequest,['randomCategorized',{'field':u'description','width':'2'}],50,''],
							[u'Checker - ' + self.topic + u' sans géométrie',"000_Checker_sans_geometrie", self.sqlRequest,['NoGeom'],'','']
							)

		super(Checker,self).load_layer()
		for self.layer in self.layers:
			i=0
			if self.layer.geometryType() == 0 : # 0, 1 and 2 are for points, lines and polygons
				self.symbols = self.layer.renderer().symbols()
				for self.symbol in self.symbols:
					self.symbol.symbolLayer(0).setName(self.markerShape[i%(len(self.markerShape)-1)])
					i=i+1
			self.iface.layerTreeView().refreshLayerSymbology(self.layer.id())
