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

from qgis.PyQt.QtCore import QCoreApplication, Qt, QLocale, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QAction, QFileDialog, QDialog, QMessageBox
from qgis.PyQt.QtGui import QIcon, QStandardItemModel, QStandardItem

from qgis.core import QgsProject, QgsLayerTreeGroup
from qgis.gui import QgisInterface

# Initialize Qt resources from file resources.py
import verivd.resources_rc  # NOQA

# Initialize layers
from verivd.help import *
from verivd.ili_validator import *
from verivd.checker import *
from verivd.verif import *
from verivd.base import *

# Import the code for the DockWidget
from .veri_vd_dockwidget import VeriVDDockWidget


class VeriVD:
    """ QGIS Plugin Implementation. """

    def __init__(self, iface: QgisInterface):
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

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

        self.dockwidget = None

    def tr(self, source_text):
        return QCoreApplication.translate('veri_vd', source_text)

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        ico = QIcon(":/plugins/verivd/icons/icon.png")
        print(ico.pixmap(32,32))
        self.actions['main'] = QAction(
            QIcon(":/plugins/verivd/icons/icon.png"),
            self.tr('Vérification des mensurations vaudoises'),
            self.iface.mainWindow())
        self.actions['main'].triggered.connect(self.run)
        self.iface.addPluginToMenu(self.menu_entry, self.actions['main'])
        self.iface.addToolBarIcon(self.actions['main'])

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        if self.dockwidget:
            self.dockwidget.close()
            self.dockwidget.deleteLater()

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

    def ouvrir_fichier(self):
        # Set the variables to global
        global model_base, model_ili_validator, model_checker, modelTest, strFile, uFile, donnees_base, donnees_topic, donnees_test

        donnees_base = (
            "Base - Tous les topics",
            "Base - Points fixes",
            "Base - Couverture du sol",
            "Base - Objets divers",
            "Base - Altimetrie",
            "Base - Nomenclature",
            "Base - Biens fonds",
            "Base - Conduite",
            "Base - Limites territoriales",
            "Base - Adresses des batiments",
            "Base - Repartition des plans"
        )
        donnees_test = (
            "Verif - Points fixes",
            "Verif - Couverture du sol et objets divers",
            "Verif - Continuite des reseaux",
            "Verif - Nomenclature",
            "Verif - Biens fonds",
            "Verif - Repartition des plans et domaine de numerotation",
            "Verif - Limites territoriales et administratives",
            "Verif - Adresses"
        )
        donnees_topic = (
            "Points fixesCategorie1",
            "Points fixesCategorie2",
            "Points fixesCategorie3",
            "Couverture du sol",
            "Objets divers",
            "Altimetrie",
            "Nomenclature",
            "Biens fonds",
            "Conduites",
            "Domaines numerotation",
            "Limites commune",
            "Limites district",
            "Limites canton",
            "Repartitions plans",
            "RepartitionNT",
            "Zones glissement",
            "NPA Localite",
            "Adresses des batiments",
            "Bords de plan"
        )
        donnees_ili_validator, donnees_checker = [], []
        file, __, = QFileDialog.getOpenFileName(
            self.dockwidget,
            'Ouvrir un fichier spatialite',
            os.path.normpath(os.path.expanduser("~/Desktop")),
            '*.sqlite'
        )

        if file:
            trace = "Fichier ouvert:\n\n{}".format(file)
            self.dockwidget.labelFile.setText(trace)
            strFile = file.encode("utf-8")
            uFile = strFile.decode("utf-8")
            i = 1
            while i <= int(self.dockwidget.tabWidget.count()):
                self.dockwidget.tabWidget.setTabEnabled(i, True)
                i += 1

            # Construct models
            model_base = QStandardItemModel()
            model_ili_validator = QStandardItemModel()
            model_checker = QStandardItemModel()
            modelTest = QStandardItemModel()
            
            for item in donnees_base:
                # Create an item with a caption
                itemBase = QStandardItem(item)
                # Add a checkbox to it
                itemBase.setCheckable(True)
                # Add the item to the model
                model_base.appendRow(itemBase)
            # Load the list in Gui
            self.dockwidget.listViewBase.setModel(model_base)
            
            for item in donnees_test:
                item_test = QStandardItem(item)
                item_test.setCheckable(True)
                modelTest.appendRow(item_test)
            self.dockwidget.listViewTest.setModel(modelTest)

            decompte_dict = SpatialiteData(self.iface, uFile)
            checker_dict = decompte_dict.load_table_list('000_checker_decompte')
            ili_validator_dict = decompte_dict.load_table_list('000_ilivalidator_decompte')
            layer_statisticsDict = decompte_dict.load_table_list('layer_statistics')

            if not ili_validator_dict:
                self.dockwidget.tabWidget.setTabEnabled(2, False)
            else:
                for topic in donnees_topic:
                    ili_validator_topic = topic.replace(' ', '_')
                    if ili_validator_topic in list(ili_validator_dict.keys()):
                        donnees_ili_validator.append('IliValidator - {}: {}'.format(
                            topic, str(ili_validator_dict[ili_validator_topic]))
                        )
            donnees_ili_validator.sort()
            for item in donnees_ili_validator:
                item_ili_validator = QStandardItem(item)
                item_ili_validator.setCheckable(True)
                model_ili_validator.appendRow(item_ili_validator)
            self.dockwidget.listViewIliValidator.setModel(model_ili_validator)

            if not checker_dict:
                self.dockwidget.tabWidget.setTabEnabled(3, False)
            else:
                for topic in donnees_topic:
                    if topic in list(checker_dict.keys()):
                        donnees_checker.append('Checker - {}: {}'.format(topic, str(checker_dict[topic])))
            donnees_checker.sort()
            for item in donnees_checker:
                item_checker = QStandardItem(item)
                item_checker.setCheckable(True)
                model_checker.appendRow(item_checker)
            self.dockwidget.listViewChecker.setModel(model_checker)
    
    def tout_effacer(self):
        # Remove all Layers
        QgsProject.instance().removeAllMapLayers()
        # Remove all Groups
        for child in  QgsProject.instance().layerTreeRoot().children():
            if isinstance(child, QgsLayerTreeGroup):
                QgsProject.instance().layerTreeRoot().removeChildNode(child)

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

        if self.dockwidget is None:
            # Create the dockwidget (after translation) and keep reference
            self.dockwidget = VeriVDDockWidget()
            self.iface.addDockWidget(Qt.TopDockWidgetArea, self.dockwidget)

        self.dockwidget.show()

        # Set the first tab to open
        self.dockwidget.tabWidget.setCurrentIndex(0)
        for i in range(1, 1+self.dockwidget.tabWidget.count()):
            self.dockwidget.tabWidget.setTabEnabled(i, False)

        # Connect the files Button and Label
        self.dockwidget.labelFile.clear()
        trace = "Pas de fichier ouvert"
        self.dockwidget.labelFile.setText(trace)
        self.dockwidget.pushButtonFichierOuvrir.clicked.connect(self.ouvrir_fichier)
        self.dockwidget.pushButtonFichierQuitter.clicked.connect(self.dockwidget.close)
        self.dockwidget.pushButtonFichierAide.clicked.connect(self.aide_fichier)
        self.dockwidget.pushButtonBaseCharger.clicked.connect(self.charger_base)
        self.dockwidget.pushButtonBaseEffacer.clicked.connect(self.tout_effacer)
        self.dockwidget.pushButtonBaseAide.clicked.connect(self.aide_base)
        self.dockwidget.pushButtonIliValidatorCharger.clicked.connect(self.charger_ili_validator)
        self.dockwidget.pushButtonIliValidatorEffacer.clicked.connect(self.tout_effacer)
        self.dockwidget.pushButtonIliValidatorAide.clicked.connect(self.aide_ili_validator)
        self.dockwidget.pushButtonCheckerCharger.clicked.connect(self.charger_checker)
        self.dockwidget.pushButtonCheckerEffacer.clicked.connect(self.tout_effacer)
        self.dockwidget.pushButtonCheckerAide.clicked.connect(self.aide_checker)
        self.dockwidget.pushButtonVerifCharger.clicked.connect(self.charger_verif)
        self.dockwidget.pushButtonVerifEffacer.clicked.connect(self.tout_effacer)
        self.dockwidget.pushButtonVerifAide.clicked.connect(self.aide_verif)
