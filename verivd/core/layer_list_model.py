# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VeriVD plugin
 Copyright (C) 2019 Denis Rouzaud
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


from qgis.PyQt.QtCore import Qt, QAbstractListModel, QModelIndex

from qgis.core import QgsProject, QgsVectorLayer, QgsLayerTreeGroup

from verivd.core.layer_info import LayerInfo
from verivd.core.spatialite_data import SpatialiteData
from verivd.core.veri_layer import VeriLayer


class InsertedLayer:
    def __init__(self, group: QgsLayerTreeGroup, layers: [QgsVectorLayer]):
        self.group = group
        self.layers = layers


class LayerListModel(QAbstractListModel):
    def __init__(self, layers: [str] = []):
        self.layers: [VeriLayer] = []
        for layer_name in layers:
            self.layers.append(VeriLayer(layer_name))
        self._spatialite_data: SpatialiteData = None
        super().__init__()

    @property
    def spatialite_data(self):
        return self._spatialite_data

    @spatialite_data.setter
    def spatialite_data(self, data):
        self._spatialite_data = data
        self.beginResetModel()
        self.reload()
        self.endResetModel()

    def reload(self):
        """
        Reloads the data when the SQLite has changed
        might be re-implemented
        """
        pass

    def layer_infos(self, layer: str) -> [LayerInfo]:
        """
        Returns the list of LayerInfo for the current category and given layer name
        Must be re-implemented
        :param layer: the layer name
        """
        return None

    def group_name(self, layer: str):
        """
        Returns the name of the group to be created in the layer tree
        might be re-implemented
        :param layer: the layer name
        """
        return layer

    def post_process_layer(self, layer: QgsVectorLayer, position: int):
        """
        Post-process the QGIS layer before adding it to the map and layer tree
        Might be reimplemented
        :param layer: the layer
        :param position: the position (index) in the group
        """
        pass

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.layers)

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        # Qt QAbstractListModel virtual method
        return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable

    def data(self, index: QModelIndex, role: int):
        # Qt QAbstractListModel virtual method
        if index.row() < 0 or index.row() >= len(self.layers):
            return None

        if role == Qt.DisplayRole:
            return self.layers[index.row()].display_name

        if role == Qt.CheckStateRole:
            return self.layers[index.row()].loaded

        return None

    def setData(self, index: QModelIndex, value, role: int) -> bool:
        # Qt QAbstractListModel virtual method
        if role == Qt.CheckStateRole:
            layer = self.layers[index.row()].name
            if value == Qt.Checked:
                self.__load_layer(layer)
            else:
                self.__unload_layer(layer)
            return True

        return False

    def __load_layer(self, layer: str):
        group_name = self.group_name(layer)
        group_layer = QgsProject.instance().layerTreeRoot().insertGroup(0, group_name)
        group_layer.setExpanded(False)
        layer_infos = self.layer_infos(layer)
        layers = self.spatialite_data.create_layers(layer_infos)
        print("YXYY", len(layer_infos), len(layers))
        for i, layer in enumerate(layers):
            self.post_process_layer(layer, i)
            QgsProject.instance().addMapLayer(layer, False)
            group_layer.insertLayer(len(self.layers), layer)
            if not layer_infos[i].visibility:
                node = QgsProject.instance().layerTreeRoot().findLayer(layer.id())
                if node:
                    node.setItemVisibilityChecked(False)
                else:
                    raise Exception("La couche n'a pas été chargée.")
            self.loaded_layers[layer] = InsertedLayer(group_layer, layers)

    def __unload_layer(self, layer: str):
        if layer not in self.loaded_layers:
            raise Exception('Layer {} is not loaded'.format(layer))
        for layer in self.loaded_layers[layer]:
            QgsProject.instance().removeMapLayer(layer)
        QgsProject.instance().layerTreeRoot().removeChildren(self.loaded_layers[layer].group)



