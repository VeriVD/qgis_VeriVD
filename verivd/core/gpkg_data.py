#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple class used to load a layer in QGIS """

# Some commonly used imports

from builtins import object
import os.path
from random import randrange
from typing import Dict

from qgis.core import (
    QgsSimpleMarkerSymbolLayerBase,
    QgsWkbTypes,
    QgsExpressionContextUtils,
    QgsVectorLayer,
    QgsPropertyCollection,
    QgsSymbol,
    QgsSimpleFillSymbolLayer,
    QgsRendererCategory,
    QgsCategorizedSymbolRenderer,
    QgsCoordinateReferenceSystem,
    QgsMarkerSymbol,
    QgsLineSymbol,
    QgsFillSymbol,
    QgsRenderContext,
)
from qgis.gui import QgisInterface
from qgis.PyQt.QtGui import QColor

from verivd.core.plugin_info import dbg_info
from verivd.core.layer_info import LayerInfo
from verivd.core.symbolgy_type import SymbologyType

MARKER_SHAPE = (
    QgsSimpleMarkerSymbolLayerBase.Square,
    QgsSimpleMarkerSymbolLayerBase.Diamond,
    QgsSimpleMarkerSymbolLayerBase.Pentagon,
    QgsSimpleMarkerSymbolLayerBase.Triangle,
    QgsSimpleMarkerSymbolLayerBase.EquilateralTriangle,
    QgsSimpleMarkerSymbolLayerBase.Star,
    QgsSimpleMarkerSymbolLayerBase.Arrow,
    QgsSimpleMarkerSymbolLayerBase.Circle,
    QgsSimpleMarkerSymbolLayerBase.ArrowHeadFilled,
)


class GpkgData(object):
    """This class Contain generic attributes and methods"""

    def __init__(self, iface: QgisInterface, gpkg_path: str):
        self.iface = iface
        self.gpkg_path = gpkg_path
        self.schema = ""
        # get the path to your plugin directory
        self.plugin_path = os.path.dirname(__file__)
        self.symbols = None
        self.properties = None
        self.layers = []

    def unique_field_finder(self, layer: QgsVectorLayer, field: str):
        fni = layer.fields().indexFromName(field)
        return layer.dataProvider().uniqueValues(fni)

    def create_simple_symbol(self, layer: QgsVectorLayer, properties: dict):
        simple_symbol = None
        if layer.geometryType() == QgsWkbTypes.PointGeometry:
            simple_symbol = QgsMarkerSymbol.createSimple(properties)
        elif layer.geometryType() == QgsWkbTypes.LineGeometry:
            simple_symbol = QgsLineSymbol.createSimple(properties)
        elif layer.geometryType() == QgsWkbTypes.PolygonGeometry:
            simple_symbol = QgsFillSymbol.createSimple(properties)

        layer.renderer().setSymbol(simple_symbol)

    def change_properties(
        self, layer: QgsVectorLayer, properties: QgsPropertyCollection
    ):
        if layer.renderer() is not None:
            # TODO check context
            context = QgsRenderContext.fromMapSettings(
                self.iface.mapCanvas().mapSettings()
            )
            context.expressionContext().appendScope(
                QgsExpressionContextUtils.layerScope(layer)
            )
            for symbol in layer.renderer().symbols(context):
                symbol.symbolLayer(0).setDataDefinedProperties(properties)
            layer.triggerRepaint()

    def create_simple_fill_symbol_layer(
        self, layer: QgsVectorLayer, fill_color: QColor
    ):
        # initialize the default symbol for this geometry type
        symbol = QgsSymbol.defaultSymbol(layer.geometryType())
        # configure a symbol layer
        symbol_layer = QgsSimpleFillSymbolLayer(fill_color)
        # replace default symbol layer with the configured one
        if symbol_layer is not None:
            symbol.changeSymbolLayer(0, symbol_layer)
        return symbol

    def random_cat_symb(self, layer: QgsVectorLayer, field: str, properties: dict):
        dbg_info(f'create categorized symbol for field "{field}"')
        categories = []
        for unique_value in self.unique_field_finder(layer, field):
            dbg_info(f"   value: {unique_value}")
            rand_color = QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256))
            symbol = self.create_simple_fill_symbol_layer(layer, fill_color=rand_color)
            category = QgsRendererCategory(unique_value, symbol, unique_value)
            # TODO: removed encode('Latin-1'), is this causing troubles?
            categories.append(category)

        renderer = QgsCategorizedSymbolRenderer(field, categories)
        if renderer is not None:
            layer.setRenderer(renderer)
            property_collection = QgsPropertyCollection()
            for key, value in properties.items():
                property_collection.setProperty(key, value)
            self.change_properties(layer, property_collection)

    def create_layer(self, display_name, schema, layer_name, sql_request=None):
        print(schema, layer_name)
        uri = f"{self.gpkg_path}|layername={layer_name}"
        if sql_request:
            uri += f"|subset={sql_request}"
        # construct the layer
        layer = QgsVectorLayer(uri, display_name, "ogr")
        if layer.isSpatial():
            layer.setCrs(QgsCoordinateReferenceSystem.fromEpsgId(2056))
        return layer

    def load_table_list(self, data_source, field_name=1, count_field=2):
        layer = self.create_layer("", self.schema, data_source)
        list_feat_dict = {}
        if layer.isValid():
            features = layer.getFeatures()
            for ft in features:
                attrs = ft.attributes()
                list_feat_dict[attrs[field_name]] = attrs[count_field]
        return list_feat_dict

    def qml_definition(self, meta_layer_name: str, layer_info: LayerInfo):
        qml_spec_file = os.path.join(
            self.plugin_path,
            "../qml",
            "{}_{}.qml".format(meta_layer_name, layer_info.layer_name),
        )
        qml_gen_file = os.path.join(
            self.plugin_path, "../qml", "{}.qml".format(layer_info.layer_name)
        )
        # Check if a specific qml file exist for this layer
        # if not, check if a generic qml file exist
        if os.path.isfile(qml_spec_file):
            return qml_spec_file
        elif os.path.isfile(qml_gen_file):
            return qml_gen_file
        dbg_info(f"{qml_spec_file} {qml_gen_file}")
        return None

    def create_layers(
        self, meta_layer_name: str, layer_infos: [LayerInfo]
    ) -> Dict[LayerInfo, QgsVectorLayer]:
        layers = {}
        for layer_info in layer_infos:
            dbg_info(f"Loading layer {layer_info.layer_name}")

            # do not set subset string now, so geometry can be correctly determined
            layer = self.create_layer(
                layer_info.display_name, self.schema, layer_info.layer_name
            )

            # Set the path to the layer's qml file. The qml file must be name at least with the layer name
            if layer.isValid() and layer.featureCount() != 0:
                if layer_info.symbology_type == SymbologyType.QML:
                    qml_file = self.qml_definition(meta_layer_name, layer_info)
                    if qml_file:
                        layer.loadNamedStyle(qml_file)
                    else:
                        self.iface.messageBar().pushWarning(
                            "VeriVD - fichier QML manquant",
                            "{} ({})".format(
                                layer_info.display_name, layer_info.layer_name
                            ),
                        )

                elif layer_info.symbology_type == SymbologyType.RANDOM_CATEGORIZED:
                    self.random_cat_symb(
                        layer,
                        layer_info.category_field,
                        layer_info.symbology_data_defined_properties,
                    )
                elif layer_info.symbology_type == SymbologyType.SIMPLE:
                    self.create_simple_symbol(layer, layer_info.symbology_properties)
                if layer_info.opacity != 1:
                    layer.setOpacity(layer_info.opacity)

                layer.setSubsetString(layer_info.sql_request)

                layers[layer_info] = layer
            else:
                layers[layer_info] = None
        return layers
