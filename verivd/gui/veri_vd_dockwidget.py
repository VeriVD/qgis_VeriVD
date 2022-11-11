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
from qgis.PyQt.QtCore import pyqtSignal, QModelIndex
from qgis.gui import QgsFileWidget
from verivd.gui.help import (
    MESSAGE_BASE,
    MESSAGE_CHECKER,
    MESSAGE_ILIVALIDATOR,
    MESSAGE_VERIF,
)

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "../ui/veri_vd_dockwidget_base.ui"))


class VeriVDDockWidget(QDockWidget, FORM_CLASS):

    file_changed = pyqtSignal(str)
    closingPlugin = pyqtSignal()

    def __init__(self, layer_models, parent=None):
        super(VeriVDDockWidget, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget.setEnabled(False)

        self.layer_models = layer_models

        self.file_widget.setDialogTitle("Ouvrir un fichier Geopackage")
        self.file_widget.setRelativeStorage(QgsFileWidget.Absolute)
        self.file_widget.setFilter("fichiers Geopackage (*.gpkg *.GPKG)")

        self.base_help_label.setText(MESSAGE_BASE)
        self.checker_help_label.setText(MESSAGE_CHECKER)
        self.ili_help_label.setText(MESSAGE_ILIVALIDATOR)
        self.verif_help_label.setText(MESSAGE_VERIF)

        self.base_list_view.setModel(layer_models.base_layer_model)
        self.verif_list_view.setModel(layer_models.verif_layer_model)
        self.ili_validator_list_view.setModel(layer_models.ili_validator_layer_model)
        self.checker_list_view.setModel(layer_models.checker_layer_model)

        layer_models.ili_validator_layer_model.modelReset.connect(self.update_ili_tab)
        layer_models.ili_validator_layer_model.dataChanged.connect(self.update_ili_tab)
        layer_models.checker_layer_model.modelReset.connect(self.update_checker_tab)
        layer_models.checker_layer_model.dataChanged.connect(self.update_checker_tab)

        self.file_widget.fileChanged.connect(self.file_changed)
        self.show_help_button.clicked.connect(self.show_help)
        self.show_help_button.click()

    def update_checker_tab(self):
        has_rows = self.layer_models.checker_layer_model.rowCount(QModelIndex()) > 0
        self.tabWidget.setTabEnabled(2, has_rows)

    def update_ili_tab(self):
        has_rows = self.layer_models.ili_validator_layer_model.rowCount(QModelIndex()) > 0
        self.tabWidget.setTabEnabled(1, has_rows)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def show_help(self, show: bool):
        self.base_help_frame.setVisible(show)
        self.checker_help_frame.setVisible(show)
        self.ili_help_frame.setVisible(show)
        self.verif_help_frame.setVisible(show)
