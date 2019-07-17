#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple class used to load a layer in QGIS """

# Some commonly used imports
from builtins import object
from qgis.core import *
from qgis.utils import iface
from qgis.PyQt.QtWidgets import QMessageBox, QDialog

# from PyQt4.QtCore import *
import os.path

# Custom imports
from random import randrange

class SpatialiteData(object):
	"""This class Contain generic attributes and methods"""
	def __init__(self, pathSQliteDB):
		self.uri = QgsDataSourceURI()
		self.schema=''
		#get the path to your plugin directory
		self.plugin_path = os.path.dirname(__file__)
		#set uri database connection
		self.uri.setDatabase(pathSQliteDB)
		self.symbols = None
		self.properties = None

	def uniqueFieldFinder(self, field):
		self.field = field
		self.fni = self.layer.fieldNameIndex(self.field) 	# based on the field's unique values
		self.unique_values = self.layer.dataProvider().uniqueValues(self.fni)
		return self.unique_values

	def createSimpleSymbol(self, **kwargs):
		self.renderer = self.layer.renderer()
		if self.layer.geometryType() == Qgis.Point:
			self.simpleSymbol = QgsMarkerSymbol.createSimple(kwargs)
		elif self.layer.geometryType() == Qgis.Line:
			self.simpleSymbol = QgsLineSymbol.createSimple(kwargs)
		elif self.layer.geometryType() == Qgis.Polygon:
			self.simpleSymbol = QgsFillSymbol.createSimple(kwargs)
		self.renderer.setSymbol(self.simpleSymbol)

	def changeProperties(self, **kwargs):
		if self.layer.renderer() is not None:
			self.properties = self.kwargs
			self.symbols = self.layer.renderer().symbols()
			for self.symbol in self.symbols:
				for self.propertie, self.propertieValue in list(self.properties.items()):
					self.symbol.symbolLayer(0).setDataDefinedProperty(self.propertie,self.propertieValue)
			self.layer.triggerRepaint()

	def createSimpleFillSymbolLayer(self, fillColor):
		# initialize the default symbol for this geometry type
		self.symbol = QgsSymbol.defaultSymbol(self.layer.geometryType())
		# configure a symbol layer
		self.layer_style = {}
		self.layer_style['color'] = fillColor
		self.symbol_layer = QgsSimpleFillSymbolLayer.create(self.layer_style)
		# replace default symbol layer with the configured one
		if self.symbol_layer is not None:
			self.symbol.changeSymbolLayer(0, self.symbol_layer)

	def randomCatSymb(self, **kwargs):
		self.field = kwargs.get('field')					#get the value with key 'field'
		self.uniqueFieldFinder(self.field)
		self.categories = []
		for self.unique_value in self.unique_values:
			self.createSimpleFillSymbolLayer('%d, %d, %d' % (randrange(0,256), randrange(0,256), randrange(0,256)))
			self.category = QgsRendererCategory(self.unique_value, self.symbol, self.unique_value.encode('Latin-1'))
			# entry for the list of category items
			self.categories.append(self.category)
		# create renderer object
		self.renderer = QgsCategorizedSymbolRenderer(self.field, self.categories)
		# assign the created renderer to the layer
		if self.renderer is not None:
			self.layer.setRenderer(self.renderer)
			self.changeProperties(**self.kwargs)

	def layerConfig(self, display_name, schema, layerName, geom_column = '', sqlRequest = ''):
		#set uri connection parameter
		self.uri.setDataSource(schema, layerName, geom_column, sqlRequest)
		#construct the layer
		self.layer = QgsVectorLayer(self.uri.uri(), display_name, 'spatialite')
		return self.layer

	def loadTableList(self, dataSource, fieldName = 1, countField = 2):
		self.layerConfig('', self.schema, dataSource,'','')
		listFeatDict={}
		if self.layer.isValid():
			features = self.layer.getFeatures()
			for ft in features:
				attrs = ft.attributes()
				listFeatDict[attrs[fieldName]] = attrs[countField]
		return listFeatDict

	def load_layer(self):
		#set the layers group in the tree
		self.groupLayer = QgsProject.instance().layerTreeRoot().insertGroup(0, self.groupName)
		self.groupLayer.setExpanded(False)
		self.layers = []
		for self.display_name, self.layerName, self.sqlRequest, self.symb, self.trans, self.visib in self.infoLayer:		#loop through layer's parameters
			if self.symb[0] !='NoGeom' :
				self.geom_column = "GEOMETRY"
			else:
				self.geom_column = ""
			self.layerConfig(self.display_name, self.schema, self.layerName, self.geom_column, self.sqlRequest)
			self.layer.crs().createFromId(2056) #Set de coordinate system to LV95
			#Set the path to the layer's qml file. The qml file must be name at least with the layer name
			if self.layer.isValid() and self.layer.featureCount() != 0:
				self.qmlSpecFile = self.plugin_path + "\\qml\\" + self.__class__.__name__ + "_" + self.layerName + ".qml"
				self.qmlGenFile = self.plugin_path + "\\qml\\" + self.layerName + ".qml"
				if self.symb[0] == 'qml':
					if os.path.isfile(self.qmlSpecFile):											#Check if a specific qml file exist for this layer
						self.layer.loadNamedStyle(self.qmlSpecFile)									#if yes add it to layer
					elif os.path.isfile(self.qmlGenFile):											#if not, check if a generic qml file exist
						self.layer.loadNamedStyle(self.qmlGenFile)									#if yes add it to layer
					else:																			#else print a warning message
						QMessageBox.warning(QDialog(), "Message", u"Il manque le fichier .qml pour la couche: " 
																+ self.display_name + '\n' + self.layerName + '\n' +
																u"Chargement d'un symbole par défault")
				elif self.symb[0] == 'randomCategorized':
					self.kwargs = self.symb[1]
					self.randomCatSymb(**self.kwargs)
				elif self.symb[0] == 'simple':
					self.kwargs = self.symb[1]
					self.createSimpleSymbol(**self.kwargs)
				if self.trans:
					self.layer.setLayerTransparency(self.trans)
				QgsProject.instance().addMapLayer(self.layer, False)
				self.groupLayer.insertLayer(len(self.layers),self.layer)
				if self.visib:
					iface.legendInterface().setLayerVisible(self.layer, False)
				self.layers.append(self.layer)
		return self.layers