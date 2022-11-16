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

from qgis.PyQt.QtCore import Qt
from qgis.core import QgsVectorLayer, QgsLayerTreeGroup


class VeriMetaLayer:
    """
    This is the base class for the data in layer list models.
    This holds information about loaded QGIS layers and layer tree information.
    1 VeriMetaLayer loads several QGIS layers.
    """

    def __init__(self, name: str, display_name: str = None):
        self._name = name
        self._display_name = display_name or name
        self._loaded = Qt.Unchecked
        self._layer_group_id = None
        self._qgis_layers: [QgsVectorLayer] = []

    @property
    def name(self):
        return self._name

    @property
    def display_name(self):
        return self._display_name

    @property
    def loaded(self):
        return self._loaded

    @loaded.setter
    def loaded(self, value: bool):
        self._loaded = value

    @property
    def layer_group_id(self):
        return self._layer_group_id

    @layer_group_id.setter
    def layer_group_id(self, value: QgsLayerTreeGroup):
        self._layer_group_id = value

    @property
    def qgis_layers(self):
        return self._qgis_layers

    @qgis_layers.setter
    def qgis_layers(self, value: [QgsVectorLayer]):
        self._qgis_layers = value
