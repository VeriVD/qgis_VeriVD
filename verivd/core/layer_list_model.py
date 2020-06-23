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

from qgis.core import QgsProject, QgsVectorLayer
from qgis.gui import QgisInterface

from verivd.core.layer_info import LayerInfo
from verivd.core.spatialite_data import SpatialiteData
from verivd.core.veri_layer import VeriLayer

Debug = True


class LayerListModel(QAbstractListModel):
    def __init__(self, iface: QgisInterface, layers: [str] = []):
        self.iface = iface
        self._veri_layers: [VeriLayer] = []
        for layer_name in layers:
            self._veri_layers.append(VeriLayer(layer_name))
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
        return len(self._veri_layers)

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        # Qt QAbstractListModel virtual method
        return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable

    def data(self, index: QModelIndex, role: int):
        # Qt QAbstractListModel virtual method
        if index.row() < 0 or index.row() >= len(self._veri_layers):
            return None

        if role == Qt.DisplayRole:
            return self._veri_layers[index.row()].display_name

        if role == Qt.CheckStateRole:
            return Qt.Checked if self._veri_layers[index.row()].loaded else Qt.Unchecked

        return None

    def setData(self, index: QModelIndex, value, role: int) -> bool:
        # Qt QAbstractListModel virtual method
        if role == Qt.CheckStateRole:
            if value == Qt.Checked:
                self.__load_layer(index)
            else:
                self.__unload_layer(index)
            self.dataChanged.emit(index, index, [Qt.CheckStateRole])
            return True
        return False

    def __load_layer(self, index: QModelIndex):
        if Debug:
            print("Load layer")
        veri_layer = self._veri_layers[index.row()]
        group_name = self.group_name(veri_layer.name)
        veri_layer.layer_tree_group = QgsProject.instance().layerTreeRoot().insertGroup(0, group_name)
        veri_layer.layer_tree_group.setExpanded(False)
        layer_infos = self.layer_infos(veri_layer.name)
        qgis_layers = self.spatialite_data.create_layers(layer_infos)
        veri_layer.qgis_layers = []
        for i, qgis_layer in enumerate(qgis_layers):
            self.post_process_layer(qgis_layer, i)
            added_qgis_layer = QgsProject.instance().addMapLayer(qgis_layer, False)
            veri_layer.layer_tree_group.insertLayer(i, added_qgis_layer)
            if not layer_infos[i].visibility:
                node = QgsProject.instance().layerTreeRoot().findLayer(added_qgis_layer.id())
                if node:
                    node.setItemVisibilityChecked(False)
                else:
                    raise Exception("La couche n'a pas été chargée.")
            veri_layer.qgis_layers.append(added_qgis_layer)
        veri_layer.loaded = True
        self.dataChanged.emit(index, index)

    def __unload_layer(self, index: QModelIndex):
        if Debug:
            print("Unload")
        veri_layer = self._veri_layers[index.row()]
        for layer in veri_layer.qgis_layers:
            QgsProject.instance().removeMapLayer(layer)
        QgsProject.instance().layerTreeRoot().removeChildNode(veri_layer.layer_tree_group)
        veri_layer.layer_tree_group = None
        veri_layer.qgis_layers = []
        veri_layer.loaded = False
        self.dataChanged.emit(index, index)



