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

from qgis.PyQt.QtCore import (
    Qt,
    QCoreApplication,
    QLocale,
    QSettings,
    QTranslator,
)
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.PyQt.QtGui import QIcon

from qgis.gui import QgisInterface

# Initialize layers
from verivd.core.plugin_info import DEBUG
from verivd.core.layer_models import LayerModels
from verivd.core.layer_list_model import LayerListModel
from verivd.core.layer_info import LayerInfo
from verivd.core.gpkg_data import GpkgData
from verivd.core.justificatif import HAS_JUSTIFICATIF

from verivd.gui.veri_vd_dockwidget import VeriVDDockWidget

TEST_FILE = "/Users/denis/Documents/temp/verivd/221116_justif.gpkg"


class VeriVD:
    """QGIS Plugin Implementation."""

    def __init__(self, iface: QgisInterface):
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        self.gpkg_data = None
        self.layer_models = LayerModels(self.iface)

        # initialize translation
        qgis_locale = QLocale(QSettings().value("locale/userLocale"))
        locale_path = os.path.join(os.path.dirname(__file__), "i18n")
        self.translator = QTranslator()
        self.translator.load(qgis_locale, "veri_vd", "_", locale_path)
        QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = {}
        self.menu_entry = self.tr("&Véri-Vaud")
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar("VeriVD")
        self.toolbar.setObjectName("VeriVD")

        self.dock_widget = None

    def tr(self, source_text):
        return QCoreApplication.translate("veri_vd", source_text)

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.actions["main"] = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), "..", "icons", "icon.png")),
            self.tr("Vérification des mensurations vaudoises"),
            self.iface.mainWindow(),
        )
        self.actions["main"].triggered.connect(self.run)
        self.iface.addPluginToMenu(self.menu_entry, self.actions["main"])
        self.iface.addToolBarIcon(self.actions["main"])

        self.dock_widget = VeriVDDockWidget(self.layer_models)
        self.iface.addDockWidget(Qt.TopDockWidgetArea, self.dock_widget)

        self.dock_widget.file_changed.connect(self.open_gpkg_file)

        for model in self.layer_models.models():
            model.layers_loaded.connect(lambda layer_name, layers_loaded, model=model: self.__on_layers_loaded(model, layer_name, layers_loaded))

        if DEBUG and os.path.exists(TEST_FILE):
            self.open_gpkg_file(TEST_FILE)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        if self.dock_widget:
            self.dock_widget.close()
            self.dock_widget.deleteLater()

        for action in self.actions.values():
            self.iface.removePluginMenu(self.menu_entry, action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    def open_gpkg_file(self, file):
        if self.gpkg_data is not None and self.layer_models.has_loaded_layer():
            if (
                QMessageBox.question(
                    self.dock_widget,
                    "Veri-VD",
                    "Voulez-vous conserver les couches chargées par {}?".format(self.gpkg_data.path),
                )
                == QMessageBox.No
            ):
                self.layer_models.unload_all_layers()
            self.layer_models.reset_models()
        if file:
            uFile = file.encode("utf-8").decode("utf-8")
            self.gpkg_data = GpkgData(self.iface, uFile)
            self.layer_models.set_gpkg_data(self.gpkg_data)
            self.dock_widget.tabWidget.setEnabled(True)
            self.dock_widget.process_justificatif_button.setEnabled(HAS_JUSTIFICATIF)
        else:
            self.gpkg_data = None
            self.dock_widget.tabWidget.setEnabled(False)
            self.dock_widget.process_justificatif_button.setEnabled(False)
            self.layer_models.set_gpkg_data(None)

    def run(self):
        """Run method that loads and starts the plugin"""
        self.dock_widget.show()

        # Set the first tab to open
        self.dock_widget.tabWidget.setCurrentIndex(0)
        self.dock_widget.tabWidget.setEnabled(False)

    def __on_layers_loaded(self, model: LayerListModel, layer_name: str, layers_loaded: [LayerInfo]):
        if model.has_control_layers:
            control_layers_loaded = 0
            layer_names = []
            for layer_info in layers_loaded:
                if layer_info.control_layer:
                    control_layers_loaded += 1
                    layer_names.append(layer_info.display_name)
            if control_layers_loaded:
                # self.iface.messageBar().pushWarning("VeriVD", 'Les scripts de vérification ont détecté des éléments problématiques pour le thème "{}:\n {}".'.format(layer_name, '\n'.join(layer_names)))
                pass
            else:
                self.iface.messageBar().pushMessage(
                    "VeriVD",
                    "Les scripts de vérification n" "ont pas détecté d" 'élément particulier pour le thème "{}".'.format(layer_name),
                )
