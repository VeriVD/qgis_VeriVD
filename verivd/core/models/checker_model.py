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


from verivd.core.layer_list_model import LayerListModel
from verivd.core.layers import DONNEES_TOPIC
from verivd.core.veri_layer import VeriLayer


class CheckerLayerModel(LayerListModel):
    def __init__(self):
        super(CheckerLayerModel, self).__init__()

    def reload(self):
        self.layers = []
        checker_dict = self.spatialite_data.load_table_list('000_checker_decompte')
        for topic in DONNEES_TOPIC:
            if topic in checker_dict:
                display_name = 'Checker - {}: {}'.format(topic, str(checker_dict[topic]))
                self.layers.append(VeriLayer(topic, display_name))