#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple class used to load a layer in QGIS """

# Some commonly used imports
from enum import Enum
from builtins import object
from qgis.core import *
from qgis.gui import QgisInterface
from qgis.utils import iface
from qgis.PyQt.QtWidgets import QMessageBox, QDialog

import os.path
from random import randrange


class SymbologyType(Enum):
	NO_SYMBOL = 1
	QML = 2
	SIMPLE = 3
	RANDOM_CATEGORIZED = 4


class LayerInfo(object):
	def __init__(
			self,
			display_name: str,
			layer_name: str,
			symbology_type: SymbologyType = SymbologyType.QML,
			symbology_properties: dict = {},
			category_field = None,
			sql_request: str = '',
			visibility: bool = True,
			opacity: float = 1
	):
		self.display_name = display_name
		self.layer_name = layer_name
		self.sql_request = sql_request
		self.symbology_type = symbology_type
		self.symbology_properties = symbology_properties
		self.category_field = category_field
		self.opacity = opacity
		self.visibility = visibility


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
		self.layers = []
		self.layer_infos = []

	def unique_field_finder(self, field):
		self.field = field
		self.fni = self.layer.fields().indexFromName(self.field)
		self.unique_values = self.layer.dataProvider().uniqueValues(self.fni)
		return self.unique_values

	def create_simple_symbol(self, properties):
		renderer = self.layer.renderer()
		if self.layer.geometryType() == QgsWkbTypes.PointGeometry:
			self.simpleSymbol = QgsMarkerSymbol.createSimple(properties)
		elif self.layer.geometryType() == QgsWkbTypes.LineGeometry:
			self.simpleSymbol = QgsLineSymbol.createSimple(properties)
		elif self.layer.geometryType() == QgsWkbTypes.PolygonGeometry:
			self.simpleSymbol = QgsFillSymbol.createSimple(properties)
		renderer.setSymbol(self.simpleSymbol)

	def change_properties(self, properties):
		if self.layer.renderer() is not None:
			# TODO check context
			context = QgsRenderContext.fromMapSettings(self.iface.mapCanvas().mapSettings())
			context.expressionContext().appendScope(QgsExpressionContextUtils.layerScope(self.layer))
			for symbol in self.layer.renderer().symbols(context):
				symbol.symbolLayer(0).setDataDefinedProperties(properties)
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

	def random_cat_symb(self, field: str, properties: dict):
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
			self.change_properties(properties)

	def layer_config(self, display_name, schema, layerName, geom_column='', sqlRequest=''):
		# set uri connection parameter
		self.uri.setDataSource(schema, layerName, geom_column, sqlRequest)
		# construct the layer
		layer = QgsVectorLayer(self.uri.uri(), display_name, 'spatialite')
		return layer

	def loadTableList(self, dataSource, fieldName=1, countField=2):
		layer = self.layer_config('', self.schema, dataSource, '', '')
		listFeatDict={}
		if layer.isValid():
			features = layer.getFeatures()
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
		for layer_info in self.layer_infos:
			if layer_info.symbology_type != SymbologyType.NO_SYMBOL :
				geom_column = "GEOMETRY"
			else:
				geom_column = ""
			layer = self.layer_config(layer_info.display_name, self.schema, layer_info.layer_name, geom_column, layer_info.sql_request)
			layer.crs().createFromId(2056) # Set de coordinate system to LV95
			# Set the path to the layer's qml file. The qml file must be name at least with the layer name
			if layer.isValid() and self.layer.featureCount() != 0:
				qml_spec_file = os.path.join(self.plugin_path, 'qml', '{}_{}.qml'.format(self.__class__.__name__, layer_info.layer_name))
				qml_gen_file = os.path.join(self.plugin_path, 'qml', '{}.qml'.format(layer_info.layer_name))
				# Check if a specific qml file exist for this layer
				# if yes add it to layer
				# if not, check if a generic qml file exist
				# if yes add it to layer
				# else print a warning message
				if layer_info.symbology_type == SymbologyType.QML:
					if os.path.isfile(qml_spec_file):
						layer.loadNamedStyle(qml_spec_file)
					elif os.path.isfile(qml_gen_file):
						layer.loadNamedStyle(qml_gen_file)
					else:
						QMessageBox.warning(
							QDialog(), "Message",
							"Il manque le fichier .qml pour la couche: {}"
							"\n{}\nChargement d'un symbole par défault".format(
								layer_info.display_name, layer_info.layer_name
							))
				elif layer_info.symbology_type == 'randomCategorized':
					self.random_cat_symb(layer_info.category_field)
				elif layer_info.symbology_type == 'simple':
					self.create_simple_symbol(layer_info.symbology_properties)
				if layer_info.opacity != 1:
					layer.setOpacity(layer_info.opacity)
				QgsProject.instance().addMapLayer(layer, False)
				group_layer.insertLayer(len(self.layers), layer)
				if not layer_info.visible:
					node = QgsProject.instance().layerTreeRoot().findLayer(layer.id()).setItemVisibilityChecked(False)
					if node:
						iface.legendInterface().setLayerVisible(layer, False)
					else:
						raise Exception("La couche n'a pas été chargée.")
				self.layers.append(layer)
