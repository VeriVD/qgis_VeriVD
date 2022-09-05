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


from qgis.PyQt.QtCore import Qt, QAbstractListModel, QModelIndex, pyqtSignal

from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsRenderContext,
    QgsExpressionContextUtils,
)
from qgis.gui import QgisInterface

from verivd.core.layer_info import LayerInfo
from verivd.core.spatialite_data import SpatialiteData
from verivd.core.veri_meta_layer import VeriMetaLayer

Debug = True


class LayerListModel(QAbstractListModel):

    # signal emitted when layers are loaded (group_name, loaded_layers)
    layers_loaded = pyqtSignal(str, list)

    def __init__(
        self,
        iface: QgisInterface,
        layers: [VeriMetaLayer] = [],
        has_control_layers: bool = False,
    ):
        """
        :param iface: the QgisInterface
        :param layers: pre-load the model with data
        :param has_control_layers: if True, the plugin will report if no control_layers have been loaded
        """
        self.iface = iface
        self._veri_meta_layers: [VeriMetaLayer] = layers
        self._spatialite_data: SpatialiteData = None
        self._has_control_layers = has_control_layers
        super().__init__()
        self.__is_removing_layer = False
        QgsProject.instance().layersWillBeRemoved.connect(self.__layers_will_be_removed)

    @property
    def spatialite_data(self):
        return self._spatialite_data

    @spatialite_data.setter
    def spatialite_data(self, data):
        self._spatialite_data = data
        self.reload()

    @property
    def veri_meta_layers(self) -> [VeriMetaLayer]:
        return self._veri_meta_layers

    @veri_meta_layers.setter
    def veri_meta_layers(self, value: [VeriMetaLayer]):
        self.beginResetModel()
        self._veri_meta_layers = value
        self.endResetModel()

    @property
    def has_control_layers(self) -> bool:
        return self._has_control_layers

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
        return len(self._veri_meta_layers)

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        # Qt QAbstractListModel virtual method
        return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable

    def data(self, index: QModelIndex, role: int):
        # Qt QAbstractListModel virtual method
        if index.row() < 0 or index.row() >= len(self._veri_meta_layers):
            return None

        if role == Qt.DisplayRole:
            return self._veri_meta_layers[index.row()].display_name

        if role == Qt.CheckStateRole:
            return self._veri_meta_layers[index.row()].loaded

        return None

    def setData(self, index: QModelIndex, value, role: int) -> bool:
        # Qt QAbstractListModel virtual method
        if role == Qt.CheckStateRole:
            if value == Qt.Checked and self.data(index, role) != Qt.PartiallyChecked:
                self.__load_layer(index)
            else:
                self.__unload_layer(index)
                self.iface.mapCanvas().refresh()
            self.dataChanged.emit(index, index, [Qt.CheckStateRole])
            return True
        return False

    def unload_all(self):
        self.beginResetModel()
        for row in range(0, self.rowCount(QModelIndex())):
            self.__unload_layer(self.index(row, 0))
        self.endResetModel()
        self.iface.mapCanvas().refresh()

    def layer_context(self, layer: QgsVectorLayer) -> QgsRenderContext:
        context = QgsRenderContext.fromMapSettings(self.iface.mapCanvas().mapSettings())
        context.expressionContext().appendScope(
            QgsExpressionContextUtils.layerScope(layer)
        )
        return context

    def __load_layer(self, index: QModelIndex):
        if Debug:
            print("Load layer")
        if not self.spatialite_data:
            return
        veri_meta_layer = self._veri_meta_layers[index.row()]
        group_name = self.group_name(veri_meta_layer.display_name)
        veri_meta_layer.layer_tree_group = (
            QgsProject.instance().layerTreeRoot().insertGroup(0, group_name)
        )
        veri_meta_layer.layer_tree_group.setExpanded(False)
        layer_infos = self.layer_infos(veri_meta_layer.name)
        layers = self.spatialite_data.create_layers(veri_meta_layer.name, layer_infos)
        veri_meta_layer.qgis_layers = []
        i = 0
        loaded_layers = []
        for layer_info, qgis_layer in layers.items():
            if qgis_layer is None:
                print("no layer loaded for {}".format(layer_info.display_name))
                continue
            self.post_process_layer(qgis_layer, i)
            added_qgis_layer = QgsProject.instance().addMapLayer(qgis_layer, False)
            veri_meta_layer.layer_tree_group.insertLayer(i, added_qgis_layer)
            if not layer_info.visibility:
                node = (
                    QgsProject.instance()
                    .layerTreeRoot()
                    .findLayer(added_qgis_layer.id())
                )
                if node:
                    node.setItemVisibilityChecked(False)
                else:
                    raise Exception(
                        'La couche "{}" n'
                        "a pas été chargée.".format(layer_info.display_name)
                    )
            loaded_layers.append(layer_info)
            veri_meta_layer.qgis_layers.append(added_qgis_layer)
            i += 1
        veri_meta_layer.loaded = Qt.Checked
        if i > 0:
            self.layers_loaded.emit(group_name, loaded_layers)

    def __unload_layer(self, index: QModelIndex):
        if Debug:
            print("Unload")
        veri_meta_layer = self._veri_meta_layers[index.row()]
        self.__is_removing_layer = True
        for layer in veri_meta_layer.qgis_layers:
            QgsProject.instance().removeMapLayer(layer)
        self.__is_removing_layer = False
        if (
            veri_meta_layer.layer_tree_group is not None
            and len(veri_meta_layer.layer_tree_group.children()) == 0
        ):
            QgsProject.instance().layerTreeRoot().removeChildNode(
                veri_meta_layer.layer_tree_group
            )
        veri_meta_layer.layer_tree_group = None
        veri_meta_layer.qgis_layers = []
        veri_meta_layer.loaded = Qt.Unchecked

    def __layers_will_be_removed(self, removed_layer_ids):
        if self.__is_removing_layer:
            return
        self.beginResetModel()
        for veri_layer in self._veri_meta_layers:
            layers_to_remove = []
            for qgis_layer in veri_layer.qgis_layers:
                for removed_layer_id in removed_layer_ids:
                    if removed_layer_id == qgis_layer.id():
                        layers_to_remove.append(qgis_layer)
            if len(layers_to_remove):
                for layer in layers_to_remove:
                    veri_layer.qgis_layers.remove(layer)
                if len(veri_layer.qgis_layers) > 0:
                    veri_layer.loaded = Qt.PartiallyChecked
                else:
                    veri_layer.loaded = Qt.Unchecked
        self.endResetModel()
