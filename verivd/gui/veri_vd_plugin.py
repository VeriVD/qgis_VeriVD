# coding: utf-8
"""
/***************************************************************************
 VeriVD
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
import os.path

from qgis.PyQt.QtCore import Qt, QCoreApplication, QLocale, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.PyQt.QtGui import QIcon

from qgis.gui import QgisInterface

# Initialize layers
from verivd.core.layer_models import LayerModels
from verivd.core.spatialite_data import SpatialiteData

from verivd.gui.veri_vd_dockwidget import VeriVDDockWidget


class VeriVD:
    """ QGIS Plugin Implementation. """

    def __init__(self, iface: QgisInterface):
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        self.spatialite_data = None
        self.layer_models = LayerModels(self.iface)

        # initialize translation
        qgis_locale = QLocale(QSettings().value('locale/userLocale'))
        locale_path = os.path.join(os.path.dirname(__file__), 'i18n')
        self.translator = QTranslator()
        self.translator.load(qgis_locale, 'veri_vd', '_', locale_path)
        QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = {}
        self.menu_entry = self.tr('&Véri-Vaud')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar('VeriVD')
        self.toolbar.setObjectName('VeriVD')

        self.dock_widget = None

    def tr(self, source_text):
        return QCoreApplication.translate('veri_vd', source_text)

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.actions['main'] = QAction(
            QIcon(":/plugins/verivd/icons/icon.png"),
            self.tr('Vérification des mensurations vaudoises'),
            self.iface.mainWindow())
        self.actions['main'].triggered.connect(self.run)
        self.iface.addPluginToMenu(self.menu_entry, self.actions['main'])
        self.iface.addToolBarIcon(self.actions['main'])

        self.dock_widget = VeriVDDockWidget(self.layer_models)
        self.iface.addDockWidget(Qt.TopDockWidgetArea, self.dock_widget)

        self.dock_widget.file_changed.connect(self.open_spatialite_file)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        if self.dock_widget:
            self.dock_widget.close()
            self.dock_widget.deleteLater()

        for action in self.actions.values():
            self.iface.removePluginMenu(self.menu_entry, action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    def open_spatialite_file(self, file):
        if self.spatialite_data is not None and self.layer_models.has_loaded_layer():
            if QMessageBox.question(
                    self.dock_widget, "Veri-VD",
                    "Voulez-vous conserver les couches chargées par {}?".format(self.spatialite_data.uri.database())
            ) == QMessageBox.No:
                self.layer_models.unload_all_layers()
            self.layer_models.reset_models()
        if file:
            strFile = file.encode("utf-8")
            uFile = strFile.decode("utf-8")
            self.spatialite_data = SpatialiteData(self.iface, uFile)
            self.layer_models.set_spatialite_data(self.spatialite_data)
            self.dock_widget.tabWidget.setEnabled(True)
        else:
            self.spatialite_data = None
            self.dock_widget.tabWidget.setEnabled(False)
            self.layer_models.set_spatialite_data(None)

    def run(self):
        """Run method that loads and starts the plugin"""
        self.dock_widget.show()

        # Set the first tab to open
        self.dock_widget.tabWidget.setCurrentIndex(0)
        self.dock_widget.tabWidget.setEnabled(False)

