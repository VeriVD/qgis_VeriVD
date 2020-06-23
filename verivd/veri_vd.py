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
import sys

from qgis.PyQt.QtCore import Qt, QCoreApplication, QLocale, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QAction, QDialog, QMessageBox
from qgis.PyQt.QtGui import QIcon

from qgis.core import QgsProject, QgsLayerTreeGroup
from qgis.gui import QgisInterface

import verivd.resources_rc

# Initialize layers
from verivd.help import *

from verivd.core.spatialite_data import SpatialiteData
from verivd.core.models.base_model import BaseLayerModel
from verivd.core.models.test_model import TestLayerModel
from verivd.core.models.checker_model import CheckerLayerModel
from verivd.core.models.ili_validator_model import IliValidatorLayerModel

from verivd.gui.veri_vd_dockwidget import VeriVDDockWidget


class LayerModels:
    def __init__(self, iface: QgisInterface):
        self.spatialite_data = None
        self.test_layer_model = TestLayerModel(iface)
        self.ili_validator_layer_model = IliValidatorLayerModel(iface)
        self.checker_layer_model = CheckerLayerModel(iface)
        self.base_layer_model = BaseLayerModel(iface)

    def set_spatialite_data(self, spatialite_data):
        self.test_layer_model.spatialite_data = spatialite_data
        self.ili_validator_layer_model.spatialite_data = spatialite_data
        self.checker_layer_model.spatialite_data = spatialite_data
        self.base_layer_model.spatialite_data = spatialite_data


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

        self.dock_widget.file_changed.connect(self.ouvrir_fichier)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        if self.dock_widget:
            self.dock_widget.close()
            self.dock_widget.deleteLater()

        for action in self.actions.values():
            self.iface.removePluginMenu(self.menu_entry, action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    def aide_fichier(self):
        QMessageBox.information(QDialog(), "Aide", Help().messageFichier)

    def aide_base(self):
        QMessageBox.information(QDialog(), "Aide", Help().messageBase)

    def aide_ili_validator(self):
        QMessageBox.information(QDialog(), "Aide", Help().messageIliValidator)

    def aide_checker(self):
        QMessageBox.information(QDialog(), "Aide", Help().messageChecker)

    def aide_verif(self):
        QMessageBox.information(QDialog(), "Aide", Help().messageVerif)

    def ouvrir_fichier(self, file):
        if file:
            self.strFile = file.encode("utf-8")
            self.uFile = self.strFile.decode("utf-8")
            i = 1
            while i <= int(self.dock_widget.tabWidget.count()):
                self.dock_widget.tabWidget.setTabEnabled(i, True)
                i += 1

            spatialite_data = SpatialiteData(self.iface, self.uFile)
            self.layer_models.set_spatialite_data(spatialite_data)

    def tout_effacer(self):
        # Remove all Layers
        QgsProject.instance().removeAllMapLayers()
        # Remove all Groups
        for child in QgsProject.instance().layerTreeRoot().children():
            if isinstance(child, QgsLayerTreeGroup):
                QgsProject.instance().layerTreeRoot().removeChildNode(child)
        self.iface.mapCanvas().refresh()

    def charger_base(self):
        # get the checked items
        checked_items = []
        for row in range(model_base.rowCount()):
            item = model_base.item(row)
        
            if item.checkState() == Qt.Checked:
                # QMessageBox.warning(QDialog(), "Message", str(item.text()))
                checked_items.append(str(item.text()).replace(" - ", "").replace(" ", "_"))
                item.setCheckState(Qt.Unchecked) 
        
        for checked_item in checked_items:
            # find the class matching the checked items
            topic_class_name = getattr(sys.modules[__name__], checked_item)
            topic = topic_class_name(self.iface, uFile)
            topic.load_layer()
            topic.infoText = ""
            for layer in topic.layers:
                topic.infoText = topic.infoText + str(layer.featureCount()) + ' ' + layer.name() + '\n'
            if topic.infoText == "":
                QMessageBox.warning(QDialog(),'Information', 'Aucun objet dans ce thème')
    
    def charger_ili_validator(self):
        # get the checked items
        checked_items = []
        for row in range(model_ili_validator.rowCount()):
            item = model_ili_validator.item(row)
            if item.checkState() == Qt.Checked:
                checked_items.append(str(item.text()).split(':')[0].replace("IliValidator - ", "").replace(" ", "_"))
                item.setCheckState(Qt.Unchecked) 

        for checked_item in checked_items:
            topic = str(checked_item)
            layersClass = IliValidator(self.iface, uFile)
            layersClass.load_layer(topic)

    def charger_checker(self):
        # get the checked items
        checked_items = []
        for row in range(model_checker.rowCount()):
            item = model_checker.item(row)
            if item.checkState() == Qt.Checked:
                checked_items.append(str(item.text()).split(':')[0].replace("Checker - ", ""))
                item.setCheckState(Qt.Unchecked) 
            
        for checked_item in checked_items:
                topic = str(checked_item)
                layersClass = Checker(self.iface, uFile)
                layersClass.load_layer(topic)

    def charger_verif(self):
        # get the checked items
        checked_items = []
        for row in range(modelTest.rowCount()):
            item = modelTest.item(row)
        
            if item.checkState() == Qt.Checked:
                checked_items.append(str(item.text()).replace(" - ", "").replace(" ", "_"))
                # QMessageBox.warning(QDialog(), "Message", checked_items[0])
                item.setCheckState(Qt.Unchecked) 
        
        for checked_item in checked_items:
                test_class_name = getattr(sys.modules[__name__], checked_item)
                test = test_class_name(self.iface, uFile)
                test.load_layer()
                test.infoText = ""
                for layer in test.layers:
                    if layer.name() in test.check_layer:
                        test.infoText = test.infoText + str(layer.featureCount()) + ' ' + layer.name() + '\n'
                if test.infoText == "":
                    QMessageBox.warning(QDialog(), "Information", "Les scripts de vérification n'ont pas détecté d'élément particulier sur ce thème.")
                #else:
                #    QMessageBox.warning(QDialog(), "Information", test.infoText)

    def run(self):
        """Run method that loads and starts the plugin"""
        self.dock_widget.show()

        # Set the first tab to open
        self.dock_widget.tabWidget.setCurrentIndex(0)
        for i in range(1, 1+self.dock_widget.tabWidget.count()):
            self.dock_widget.tabWidget.setTabEnabled(i, False)

        # Connect the files Button and Label
        self.dock_widget.labelFile.clear()
        trace = "Pas de fichier ouvert"
        self.dock_widget.labelFile.setText(trace)
        self.dock_widget.pushButtonFichierOuvrir.clicked.connect(self.ouvrir_fichier)
        self.dock_widget.pushButtonFichierQuitter.clicked.connect(self.dock_widget.close)
        self.dock_widget.pushButtonFichierAide.clicked.connect(self.aide_fichier)
        self.dock_widget.pushButtonBaseCharger.clicked.connect(self.charger_base)
        self.dock_widget.pushButtonBaseEffacer.clicked.connect(self.tout_effacer)
        self.dock_widget.pushButtonBaseAide.clicked.connect(self.aide_base)
        self.dock_widget.pushButtonIliValidatorCharger.clicked.connect(self.charger_ili_validator)
        self.dock_widget.pushButtonIliValidatorEffacer.clicked.connect(self.tout_effacer)
        self.dock_widget.pushButtonIliValidatorAide.clicked.connect(self.aide_ili_validator)
        self.dock_widget.pushButtonCheckerCharger.clicked.connect(self.charger_checker)
        self.dock_widget.pushButtonCheckerEffacer.clicked.connect(self.tout_effacer)
        self.dock_widget.pushButtonCheckerAide.clicked.connect(self.aide_checker)
        self.dock_widget.pushButtonVerifCharger.clicked.connect(self.charger_verif)
        self.dock_widget.pushButtonVerifEffacer.clicked.connect(self.tout_effacer)
        self.dock_widget.pushButtonVerifAide.clicked.connect(self.aide_verif)
