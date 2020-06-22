# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VeriVDDockWidget
                                 A QGIS plugin
 Vérification des mensurations vaudoises
                             -------------------
        begin                : 2018-11-15
        git sha              : $Format:%H$
        copyright            : (C) 2018 by FSN/OIT
        email                : fabien.simon@vd.ch
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

import os

from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDockWidget
from qgis.PyQt.QtCore import pyqtSignal
from qgis.gui import QgsFileWidget
from verivd.core.layer_list_model import LayerModels


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), '../ui/veri_vd_dockwidget_base.ui'
))


class VeriVDDockWidget(QDockWidget, FORM_CLASS):

    file_changed = pyqtSignal(str)
    closingPlugin = pyqtSignal()

    def __init__(self, layer_models: LayerModels, parent=None):
        super(VeriVDDockWidget, self).__init__(parent)
        self.setupUi(self)

        self.file_widget.setDialogTitle('Ouvrir un fichier spatialite')
        self.file_widget.setRelativeStorage(QgsFileWidget.Absolute)
        self.file_widget.setSelectedFilter('*.sqlite')

        self.base_list_view.setModel(layer_models.base_layer_model)
        self.test_list_view.setModel(layer_models.test_layer_model)
        self.ili_validator_list_view.setModel(layer_models.ili_validator_layer_model)
        self.checker_list_view.setModel(layer_models.checker_layer_model)

        self.file_widget.fileChanged.connect(self.file_changed)


    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

