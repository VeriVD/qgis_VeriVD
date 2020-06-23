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

start_app()


class OfflineConverterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.iface = get_iface()

    def setUp(self):
        pass

    def test_base_model_completeness(self):
        model = BaseLayerModel(self.iface)
        for layer in model._veri_layers:
            self.assertTrue(layer.name in BASE_LAYER_INFOS, layer.name)

    def test_verif_model_completeness(self):
        model = VerifLayerModel(self.iface)
        for layer in model._veri_layers:
            self.assertTrue(layer.name in VERIF_LAYER_INFOS, layer.name)