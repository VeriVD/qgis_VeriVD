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

from qgis.core import QgsProject
from qgis.gui import QgisInterface

from verivd.core.layer_list_model import LayerListModel
from verivd.core.models.base_model import BaseLayerModel
from verivd.core.models.checker_model import CheckerLayerModel
from verivd.core.models.ili_validator_model import IliValidatorLayerModel
from verivd.core.models.verif_model import VerifLayerModel


class LayerModels:
    def __init__(self, iface: QgisInterface):
        self.spatialite_data = None
        self.verif_layer_model = VerifLayerModel(iface)
        self.ili_validator_layer_model = IliValidatorLayerModel(iface)
        self.checker_layer_model = CheckerLayerModel(iface)
        self.base_layer_model = BaseLayerModel(iface)

    def set_spatialite_data(self, spatialite_data):
        self.verif_layer_model.spatialite_data = spatialite_data
        self.ili_validator_layer_model.spatialite_data = spatialite_data
        self.checker_layer_model.spatialite_data = spatialite_data
        self.base_layer_model.spatialite_data = spatialite_data

    def unload_all_layers(self):
        self.verif_layer_model.unload_all()
        self.ili_validator_layer_model.unload_all()
        self.checker_layer_model.unload_all()
        self.base_layer_model.unload_all()

    def models(self) -> [LayerListModel]:
        return (self.verif_layer_model, self.ili_validator_layer_model,
                self.checker_layer_model, self.base_layer_model)

    def has_loaded_layer(self) -> bool:
        """
        Returns if any of the models has a loaded layer
        """
        for model in self.models():
            for layer in model._veri_meta_layers:
                if layer.loaded:
                    return True
        return False

