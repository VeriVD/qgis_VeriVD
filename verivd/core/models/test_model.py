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

from qgis.gui import QgisInterface

from verivd.core.layer_list_model import LayerListModel
from verivd.core.layers import DONNEES_TEST


class TestLayerModel(LayerListModel):
    def __init__(self, iface: QgisInterface):
        super(TestLayerModel, self).__init__(iface, DONNEES_TEST)
