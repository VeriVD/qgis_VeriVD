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

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'veri_vd_dockwidget_base.ui'
))


class VeriVDDockWidget(QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(VeriVDDockWidget, self).__init__(parent)
        self.setupUi(self)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

