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

from qgis.testing import start_app, unittest
from qgis.testing.mocked import get_iface

from verivd.core.models.base_model import BASE_LAYER_INFOS, BaseLayerModel
from verivd.core.models.verif_model import VERIF_LAYER_INFOS, VerifLayerModel
from verivd.core.spatialite_data import SpatialiteData
from verivd.core.layer_models import LayerModels
from verivd.core.symbolgy_type import SymbologyType


start_app()

DATA_PATH = "133_AF2_2440_NUM.sqlite"

MISSING_QML = ("101_verif_ddp_segment_bf_modifie",)


class OfflineConverterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.iface = get_iface()

    def setUp(self):
        pass

    def test_base_model_completeness(self):
        model = BaseLayerModel(self.iface)
        for layer in model._veri_meta_layers:
            self.assertTrue(layer.name in BASE_LAYER_INFOS, layer.name)

    def test_verif_model_completeness(self):
        model = VerifLayerModel(self.iface)
        for layer in model._veri_meta_layers:
            self.assertTrue(layer.name in VERIF_LAYER_INFOS, layer.name)

    def test_qml(self):
        layer_models = LayerModels(self.iface)
        spatialite_data = SpatialiteData(self.iface, DATA_PATH)
        layer_models.set_spatialite_data(spatialite_data)
        for model in layer_models.models():
            for veri_layer in model._veri_meta_layers:
                layer_infos = model.layer_infos(veri_layer.name)
                for layer_info in layer_infos:
                    if layer_info.symbology_type == SymbologyType.QML:
                        if layer_info.layer_name in MISSING_QML:
                            continue
                        self.assertIsNotNone(
                            spatialite_data.qml_definition(veri_layer.name, layer_info),
                            "Layer {} has no QML file".format(layer_info.layer_name),
                        )
