#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple class used to load a layer in QGIS """

# Some commonly used imports
from builtins import object
from qgis.core import *
from qgis.gui import QgisInterface
from qgis.utils import iface
from qgis.PyQt.QtWidgets import QMessageBox, QDialog

import os.path
from random import randrange


class SpatialiteData(object):
	"""This class Contain generic attributes and methods"""
	def __init__(self, iface: QgisInterface, pathSQliteDB: str):
		self.iface = iface
		self.uri = QgsDataSourceUri()
		self.schema = ''
		# get the path to your plugin directory
		self.plugin_path = os.path.dirname(__file__)
		# set uri database connection
		self.uri.setDatabase(pathSQliteDB)
		self.symbols = None
		self.properties = None
		self.infoLayer = []

	def unique_field_finder(self, field):
		self.field = field
		self.fni = self.layer.fields().indexFromName(self.field)
		self.unique_values = self.layer.dataProvider().uniqueValues(self.fni)
		return self.unique_values

	def create_simple_symbol(self, **kwargs):
		renderer = self.layer.renderer()
		if self.layer.geometryType() == QgsWkbTypes.PointGeometry:
			self.simpleSymbol = QgsMarkerSymbol.createSimple(kwargs)
		elif self.layer.geometryType() == QgsWkbTypes.LineGeometry:
			self.simpleSymbol = QgsLineSymbol.createSimple(kwargs)
		elif self.layer.geometryType() == QgsWkbTypes.PolygonGeometry:
			self.simpleSymbol = QgsFillSymbol.createSimple(kwargs)
		renderer.setSymbol(self.simpleSymbol)

	def change_properties(self, **kwargs):
		if self.layer.renderer() is not None:
			self.properties = self.kwargs
			# TODO check context
			context = QgsRenderContext.fromMapSettings(self.iface.mapCanvas().mapSettings())
			context.expressionContext().appendScope(QgsExpressionContextUtils.layerScope(self.layer))
			self.symbols = self.layer.renderer().symbols(context)
			for self.symbol in self.symbols:
				for property_key, property_value in list(self.properties.items()):
					self.symbol.symbolLayer(0).setDataDefinedProperty(property_key, property_value)
			self.layer.triggerRepaint()

	def create_simple_fill_symbol_layer(self, fillColor):
		# initialize the default symbol for this geometry type
		self.symbol = QgsSymbol.defaultSymbol(self.layer.geometryType())
		# configure a symbol layer
		self.layer_style = {}
		self.layer_style['color'] = fillColor
		self.symbol_layer = QgsSimpleFillSymbolLayer.create(self.layer_style)
		# replace default symbol layer with the configured one
		if self.symbol_layer is not None:
			self.symbol.changeSymbolLayer(0, self.symbol_layer)

	def random_cat_symb(self, **kwargs):
		field = kwargs.get('field')  # get the value with key 'field'
		self.unique_field_finder(field)
		categories = []
		for self.unique_value in self.unique_values:
			self.create_simple_fill_symbol_layer('%d, %d, %d' % (randrange(0, 256), randrange(0, 256), randrange(0, 256)))
			category = QgsRendererCategory(self.unique_value, self.symbol, self.unique_value)  # TODO: removed encode('Latin-1'), is this causing troubles?
			# entry for the list of category items
			categories.append(category)
		# create renderer object
		self.renderer = QgsCategorizedSymbolRenderer(self.field, categories)
		# assign the created renderer to the layer
		if self.renderer is not None:
			self.layer.setRenderer(self.renderer)
			self.change_properties(**self.kwargs)

	def layer_config(self, display_name, schema, layerName, geom_column='', sqlRequest=''):
		# set uri connection parameter
		self.uri.setDataSource(schema, layerName, geom_column, sqlRequest)
		# construct the layer
		self.layer = QgsVectorLayer(self.uri.uri(), display_name, 'spatialite')
		return self.layer

	def loadTableList(self, dataSource, fieldName=1, countField=2):
		self.layer_config('', self.schema, dataSource, '', '')
		listFeatDict={}
		if self.layer.isValid():
			features = self.layer.getFeatures()
			for ft in features:
				attrs = ft.attributes()
				listFeatDict[attrs[fieldName]] = attrs[countField]
		return listFeatDict

	def load_layer(self):
		# set the layers group in the tree
		group_layer = QgsProject.instance().layerTreeRoot().insertGroup(0, self.group_name)
		group_layer.setExpanded(False)
		self.layers = []
		# loop through layer's parameters
		for display_name, layerName, sqlRequest, symb, trans, visib in self.infoLayer:
			if symb[0] !='NoGeom' :
				geom_column = "GEOMETRY"
			else:
				geom_column = ""
			self.layer_config(display_name, self.schema, layerName, geom_column, sqlRequest)
			self.layer.crs().createFromId(2056) # Set de coordinate system to LV95
			# Set the path to the layer's qml file. The qml file must be name at least with the layer name
			if self.layer.isValid() and self.layer.featureCount() != 0:
				qml_spec_file = os.path.join(self.plugin_path, 'qml', '{}_{}.qml'.format(self.__class__.__name__, layerName))
				qml_gen_file = os.path.join(self.plugin_path, 'qml', '{}.qml'.format(layerName))
				# Check if a specific qml file exist for this layer
				# if yes add it to layer
				# if not, check if a generic qml file exist
				# if yes add it to layer
				# else print a warning message
				if symb[0] == 'qml':
					if os.path.isfile(qml_spec_file):
						self.layer.loadNamedStyle(qml_spec_file)
					elif os.path.isfile(qml_gen_file):
						self.layer.loadNamedStyle(qml_gen_file)
					else:
						QMessageBox.warning(
							QDialog(), "Message",
							"Il manque le fichier .qml pour la couche: {}"
							"\n{}\nChargement d'un symbole par défault".format(
								display_name, layerName
							))
				elif symb[0] == 'randomCategorized':
					self.kwargs = symb[1]
					self.random_cat_symb(**self.kwargs)
				elif symb[0] == 'simple':
					self.kwargs = symb[1]
					self.create_simple_symbol(**self.kwargs)
				if trans:
					self.layer.setLayerTransparency(trans)
				QgsProject.instance().addMapLayer(self.layer, False)
				group_layer.insertLayer(len(self.layers),self.layer)
				if visib:
					iface.legendInterface().setLayerVisible(self.layer, False)
				self.layers.append(self.layer)
