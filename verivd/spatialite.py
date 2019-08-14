#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple class used to load a layer in QGIS """

# Some commonly used imports
from enum import Enum
from builtins import object
from qgis.core import *
from qgis.gui import QgisInterface
from qgis.utils import iface
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtWidgets import QMessageBox, QDialog

import os.path
from random import randrange

MARKER_SHAPE = (
	QgsSimpleMarkerSymbolLayerBase.Square,
	QgsSimpleMarkerSymbolLayerBase.Diamond,
	QgsSimpleMarkerSymbolLayerBase.Pentagon,
	QgsSimpleMarkerSymbolLayerBase.Triangle,
	QgsSimpleMarkerSymbolLayerBase.EquilateralTriangle,
	QgsSimpleMarkerSymbolLayerBase.Star,
	QgsSimpleMarkerSymbolLayerBase.Arrow,
	QgsSimpleMarkerSymbolLayerBase.Circle,
	QgsSimpleMarkerSymbolLayerBase.ArrowHeadFilled
)


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

	def unique_field_finder(self, layer: QgsVectorLayer, field: str):
		fni = layer.fields().indexFromName(field)
		return layer.dataProvider().uniqueValues(fni)

	def create_simple_symbol(self, layer: QgsVectorLayer, properties):
		renderer = layer.renderer()
		simple_symbol = None
		if layer.geometryType() == QgsWkbTypes.PointGeometry:
			simple_symbol = QgsMarkerSymbol.createSimple(properties)
		elif layer.geometryType() == QgsWkbTypes.LineGeometry:
			simple_symbol = QgsLineSymbol.createSimple(properties)
		elif layer.geometryType() == QgsWkbTypes.PolygonGeometry:
			simple_symbol = QgsFillSymbol.createSimple(properties)
		renderer.setSymbol(simple_symbol)

	def change_properties(self, layer: QgsVectorLayer, properties: QgsPropertyCollection):
		if layer.renderer() is not None:
			# TODO check context
			context = QgsRenderContext.fromMapSettings(self.iface.mapCanvas().mapSettings())
			context.expressionContext().appendScope(QgsExpressionContextUtils.layerScope(layer))
			for symbol in layer.renderer().symbols(context):
				symbol.symbolLayer(0).setDataDefinedProperties(properties)
			layer.triggerRepaint()

	def create_simple_fill_symbol_layer(self, layer: QgsVectorLayer, fill_color: QColor):
		# initialize the default symbol for this geometry type
		symbol = QgsSymbol.defaultSymbol(layer.geometryType())
		# configure a symbol layer
		symbol_layer = QgsSimpleFillSymbolLayer(fill_color)
		# replace default symbol layer with the configured one
		if symbol_layer is not None:
			symbol.changeSymbolLayer(0, symbol_layer)
		return symbol

	def random_cat_symb(self, layer: QgsVectorLayer, field: str, properties: dict):
		categories = []
		for unique_value in self.unique_field_finder(layer, field):
			symbol = self.create_simple_fill_symbol_layer(
				layer, fill_color=QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256)))
			category = QgsRendererCategory(unique_value, symbol, unique_value)  # TODO: removed encode('Latin-1'), is this causing troubles?
			# entry for the list of category items
			categories.append(category)
		# create renderer object
		renderer = QgsCategorizedSymbolRenderer(field, categories)
		# assign the created renderer to the layer
		if renderer is not None:
			layer.setRenderer(renderer)
			property_collection = QgsPropertyCollection()
			for key, value in properties.items():
				property_collection.setProperty(key, value)
			self.change_properties(layer, property_collection)

	def layer_config(self, display_name, schema, layer_name, geom_column='', sql_request=''):
		# set uri connection parameter
		self.uri.setDataSource(schema, layer_name, geom_column, sql_request)
		# construct the layer
		layer = QgsVectorLayer(self.uri.uri(), display_name, 'spatialite')
		return layer

	def load_table_list(self, data_source, field_name=1, count_field=2):
		layer = self.layer_config('', self.schema, data_source, '', '')
		list_feat_dict = {}
		if layer.isValid():
			features = layer.getFeatures()
			for ft in features:
				attrs = ft.attributes()
				list_feat_dict[attrs[field_name]] = attrs[count_field]
		return list_feat_dict

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
			if layer.isValid() and layer.featureCount() != 0:
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
				elif layer_info.symbology_type == SymbologyType.RANDOM_CATEGORIZED:
					self.random_cat_symb(layer, layer_info.category_field, layer_info.symbology_properties)
				elif layer_info.symbology_type == SymbologyType.SIMPLE:
					self.create_simple_symbol(layer, layer_info.symbology_properties)
				if layer_info.opacity != 1:
					layer.setOpacity(layer_info.opacity)
				QgsProject.instance().addMapLayer(layer, False)
				group_layer.insertLayer(len(self.layers), layer)
				if not layer_info.visibility:
					node = QgsProject.instance().layerTreeRoot().findLayer(layer.id())
					if node:
						node.setItemVisibilityChecked(False)
					else:
						raise Exception("La couche n'a pas été chargée.")
				self.layers.append(layer)
