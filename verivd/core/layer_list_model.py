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


from qgis.PyQt.QtCore import Qt, QStringListModel, QModelIndex
from verivd.core.layers import DONNEES_TOPIC, DONNEES_TEST, DONNEES_BASE


class LayerListModel(QStringListModel):
    def __init__(self, *args, **kwargs):
        super(QStringListModel, self).__init__(*args, **kwargs)
        self.loaded_layers = []

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable

    def data(self, index: QModelIndex, role: int):
        if role == Qt.CheckStateRole:
            return self.data(index, Qt.DisplayRole) in self.loaded_layers

        return QStringListModel.data(self, index, role)

    def setData(self, index: QModelIndex, value, role: int) -> bool:
        if role == Qt.CheckStateRole:
            return True

        return QStringListModel.data(self, index, value, role)


class IliValidatorLayerModel(LayerListModel):
    def __init__(self):
        super(LayerListModel, self).__init__()

    def set_ili_validator_data(self, ili_validator_dict: dict):
        donnees_ili_validator = []
        for topic in DONNEES_TOPIC:
            ili_validator_topic = topic.replace(' ', '_')
            if ili_validator_topic in list(ili_validator_dict.keys()):
                donnees_ili_validator.append('IliValidator - {}: {}'.format(
                    topic, str(ili_validator_dict[ili_validator_topic])
                ))
        donnees_ili_validator.sort()
        self.setStringList(donnees_ili_validator)


class CheckerLayerModel(LayerListModel):
    def __init__(self):
        super(LayerListModel, self).__init__()

    def set_checker_data(self, checker_dict: dict):
        donnees_checker = []
        for topic in DONNEES_TOPIC:
            if topic in checker_dict:
                donnees_checker.append('Checker - {}: {}'.format(topic, str(checker_dict[topic])))
        donnees_checker.sort()
        self.setStringList(donnees_checker)


class TestLayerModel(LayerListModel):
    def __init__(self):
        super(LayerListModel, self).__init__(DONNEES_TEST)


class BaseLayerModel(LayerListModel):
    def __init__(self):
        super(LayerListModel, self).__init__(DONNEES_BASE)


class LayerModels():
    def __init__(self):
        self.test_layer_model = TestLayerModel()
        self.ili_validator_layer_model = IliValidatorLayerModel()
        self.checker_layer_model = CheckerLayerModel()
        self.base_layer_model = BaseLayerModel()
