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
from __future__ import absolute_import
from builtins import str
from builtins import range
from builtins import object
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt, QObject 
from qgis.PyQt.QtWidgets import QAction, QFileDialog, QDialog, QMessageBox
from qgis.PyQt.QtGui import QIcon, QStandardItemModel, QStandardItem
from qgis.PyQt import QtGui, uic
from qgis.core import QgsProject, QgsProject, QgsLayerTreeGroup

# Initialize Qt resources from file resources.py
from . import resources

# Initialize layers
from .help import *
from .base import *
from .iliValidator import *
from .checker import *
from .verif import *

# Import the code for the DockWidget
from .veriVD_dockwidget import VeriVDDockWidget
import os.path, sys


class VeriVD(object):
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgisInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'VeriVD_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Véri-Vaud')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'VeriVD')
        self.toolbar.setObjectName(u'VeriVD')

        #print "** INITIALIZING VeriVD"

        self.pluginIsActive = False
        self.dockwidget = None


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('VeriVD', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/VeriVD/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Vérification des mensurations vaudoises'),
            callback=self.run,
            parent=self.iface.mainWindow())

    #--------------------------------------------------------------------------

    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        #print "** CLOSING VeriVD"

        # disconnects
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)

        # remove this statement if dockwidget is to remain
        # for reuse if plugin is reopened
        # Commented next statement since it causes QGIS crashe
        # when closing the docked window:
        # self.dockwidget = None

        self.pluginIsActive = False


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        #print "** UNLOAD VeriVD"

        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Véri-Vaud'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    #--------------------------------------------------------------------------

    def aideFichier(self):
        QMessageBox.information(QDialog(), "Aide", Help().messageFichier)

    def aideBase(self):
        QMessageBox.information(QDialog(), "Aide", Help().messageBase)

    def aideIliValidator(self):
        QMessageBox.information(QDialog(), "Aide", Help().messageIliValidator)

    def aideChecker(self):
        QMessageBox.information(QDialog(), "Aide", Help().messageChecker)

    def aideVerif(self):
        QMessageBox.information(QDialog(), "Aide", Help().messageVerif)

    def ouvrirFichier(self):
        #Set the variables to global 
        global modelBase, modelIliValidator, modelChecker, modelTest, strFile, uFile, donneesBase, donneesTopic, donneesTest

        #Set plugin's variables

        donneesBase = (u"Base - Tous les topics", u"Base - Points fixes", u"Base - Couverture du sol",u"Base - Objets divers",u"Base - Altimetrie",u"Base - Nomenclature",u"Base - Biens fonds",u"Base - Conduite",u"Base - Limites territoriales",u"Base - Adresses des batiments",u"Base - Repartition des plans")
        donneesTest = (u"Verif - Points fixes", u"Verif - Couverture du sol et objets divers", u"Verif - Continuite des reseaux", u"Verif - Nomenclature", u"Verif - Biens fonds", u"Verif - Repartition des plans et domaine de numerotation",u"Verif - Limites territoriales et administratives", u"Verif - Adresses")
        donneesTopic = (u"Points fixesCategorie1",u"Points fixesCategorie2",u"Points fixesCategorie3",u"Couverture du sol","Objets divers",u"Altimetrie",u"Nomenclature",u"Biens fonds",u"Conduites",u"Domaines numerotation",u"Limites commune",u"Limites district",u"Limites canton",u"Repartitions plans",u"RepartitionNT",u"Zones glissement",u"NPA Localite",u"Adresses des batiments",u"Bords de plan")
        donneesIliValidator, donneesChecker = [], []
        file, __, __ = QFileDialog.getOpenFileName(self.dockwidget, 'Ouvrir un fichier spatialite',os.path.join(os.environ["HOMEPATH"], "Desktop"), '*.sqlite')

        if file != '':
            trace = "Fichier ouvert:\n\n" + file
            self.dockwidget.labelFile.setText(trace)
            strFile =  file.encode("utf-8")
            uFile = strFile.decode("utf-8")
            i = 1
            while i <= int(self.dockwidget.tabWidget.count()):
                self.dockwidget.tabWidget.setTabEnabled(i,True)
                i += 1

            #Construct models 
            modelBase, modelIliValidator, modelChecker, modelTest = QStandardItemModel(), QStandardItemModel(), QStandardItemModel(), QStandardItemModel()
            
            for item in donneesBase:
                # Create an item with a caption
                itemBase = QStandardItem(item)
                # Add a checkbox to it
                itemBase.setCheckable(True)
                # Add the item to the model
                modelBase.appendRow(itemBase)
            #Load the list in Gui
            self.dockwidget.listViewBase.setModel(modelBase)
            
            for item in donneesTest:
                itemTest = QStandardItem(item)
                itemTest.setCheckable(True)
                modelTest.appendRow(itemTest)
            self.dockwidget.listViewTest.setModel(modelTest)

            DecompteDict = SpatialiteData(uFile)
            CheckerDict = DecompteDict.loadTableList('000_checker_decompte')
            ilivalidatorDict = DecompteDict.loadTableList('000_ilivalidator_decompte')
            layer_statisticsDict = DecompteDict.loadTableList('layer_statistics')

            if not ilivalidatorDict:
                self.dockwidget.tabWidget.setTabEnabled(2,False)
            else:
                for topic in donneesTopic:
                    iliValidatorTopic = topic.replace(' ','_')
                    if iliValidatorTopic in list(ilivalidatorDict.keys()):
                        donneesIliValidator.append("IliValidator - " + topic + ': ' + str(ilivalidatorDict[iliValidatorTopic]))
            donneesIliValidator.sort()
            for item in donneesIliValidator:
                itemIliValidator = QStandardItem(item)
                itemIliValidator.setCheckable(True)
                modelIliValidator.appendRow(itemIliValidator)
            self.dockwidget.listViewIliValidator.setModel(modelIliValidator)    

            if not CheckerDict:
                self.dockwidget.tabWidget.setTabEnabled(3,False)
            else:
                for topic in donneesTopic:
                    if topic in list(CheckerDict.keys()):
                        donneesChecker.append("Checker - " + topic + ': ' + str(CheckerDict[topic]))
            donneesChecker.sort()
            for item in donneesChecker:
                itemChecker = QStandardItem(item)
                itemChecker.setCheckable(True)
                modelChecker.appendRow(itemChecker)
            self.dockwidget.listViewChecker.setModel(modelChecker)
    
    def toutEffacer(self):
        #Remove all Layers
        QgsProject.instance().removeAllMapLayers()
        #Remove all Groups
        for child in  QgsProject.instance().layerTreeRoot().children():
            if isinstance(child, QgsLayerTreeGroup):
                QgsProject.instance().layerTreeRoot().removeChildNode(child)

    def chargerBase(self):
        # get the checked items
        checked_items = []
        for row in range(modelBase.rowCount()):
            item = modelBase.item(row)
        
            if item.checkState() == Qt.Checked:
                #QMessageBox.warning(QDialog(), "Message", str(item.text()))
                checked_items.append(str(item.text()).replace(" - ","").replace(" ","_"))
                item.setCheckState(Qt.Unchecked) 
        
        for checked_item in checked_items:
                topicClassName = getattr(sys.modules[__name__], checked_item)		#find the class matching the checked items
                Topic = topicClassName(uFile)
                Topic.layers = Topic.load_layer()
                Topic.infoText = u""
                for Topic.layer in Topic.layers:
                    Topic.infoText = Topic.infoText + str(Topic.layer.featureCount()) + ' ' + Topic.layer.name() + '\n'
                if Topic.infoText == "":
                    QMessageBox.warning(QDialog(), "Information", u"Aucun objet dans ce thème.")
    
    def chargerIliValidator(self):
        # get the checked items
        checked_items = []
        for row in range(modelIliValidator.rowCount()):    
            item = modelIliValidator.item(row)
            if item.checkState() == Qt.Checked:
                checked_items.append(str(item.text()).split(':')[0].replace("IliValidator - ","").replace(" ","_"))
                item.setCheckState(Qt.Unchecked) 

        for checked_item in checked_items:
                topic = str(checked_item)
                layersClass = IliValidator(self.iface, uFile)
                layersClass.load_layer(topic)

    def chargerChecker(self):
        # get the checked items
        checked_items = []
        for row in range(modelChecker.rowCount()):    
            item = modelChecker.item(row)
            if item.checkState() == Qt.Checked:
                checked_items.append(str(item.text()).split(':')[0].replace("Checker - ",""))
                item.setCheckState(Qt.Unchecked) 
            
        for checked_item in checked_items:
                topic = str(checked_item)
                layersClass = Checker(self.iface, uFile)
                layersClass.load_layer(topic)

    def chargerVerif(self):
        # get the checked items
        checked_items = []
        for row in range(modelTest.rowCount()):
            item = modelTest.item(row)
        
            if item.checkState() == Qt.Checked:
                checked_items.append(str(item.text()).replace(" - ","").replace(" ","_"))
                #QMessageBox.warning(QDialog(), "Message", checked_items[0])
                item.setCheckState(Qt.Unchecked) 
        
        for checked_item in checked_items:
                testClassName = getattr(sys.modules[__name__], checked_item)
                Test = testClassName(uFile)
                Test.layers = Test.load_layer()
                Test.infoText = u""
                for Test.layer in Test.layers:
                    if Test.layer.name() in Test.checkLayer:
                        Test.infoText = Test.infoText + str(Test.layer.featureCount()) + ' ' + Test.layer.name() + '\n'
                if Test.infoText == "":
                    QMessageBox.warning(QDialog(), "Information", u"Les scripts de vérification n'ont pas détecté d'élément particulier sur ce thème.")
                #else:
                #    QMessageBox.warning(QDialog(), "Information", test.infoText)
    #--------------------------------------------------------------------------
    def run(self):
        """Run method that loads and starts the plugin"""

        if not self.pluginIsActive:
            self.pluginIsActive = True

            #print "** STARTING VeriVD"

            # dockwidget may not exist if:
            #    first run of plugin
            #    removed on close (see self.onClosePlugin method)
            if self.dockwidget == None:
                # Create the dockwidget (after translation) and keep reference
                self.dockwidget = VeriVDDockWidget()

            # connect to provide cleanup on closing of dockwidget
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)

            # show the dockwidget
            # TODO: fix to allow choice of dock location
            self.iface.addDockWidget(Qt.TopDockWidgetArea, self.dockwidget)
            self.dockwidget.show()

            # connect to provide cleanup on closing of dockwidget
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)

        # Set the first tab to open
        self.dockwidget.tabWidget.setCurrentIndex(0)
        i = 1
        while i <= int(self.dockwidget.tabWidget.count()):
            self.dockwidget.tabWidget.setTabEnabled(i,False)
            i += 1

        #Connect the files Button and Label
        self.dockwidget.labelFile.clear()
        trace = "Pas de fichier ouvert"
        self.dockwidget.labelFile.setText(trace)
        self.dockwidget.pushButtonFichierOuvrir.clicked.connect(self.ouvrirFichier)
        self.dockwidget.pushButtonFichierQuitter.clicked.connect(self.dockwidget.close)
        self.dockwidget.pushButtonFichierAide.clicked.connect(self.aideFichier)
        self.dockwidget.pushButtonBaseCharger.clicked.connect(self.chargerBase)
        self.dockwidget.pushButtonBaseEffacer.clicked.connect(self.toutEffacer)
        self.dockwidget.pushButtonBaseAide.clicked.connect(self.aideBase)
        self.dockwidget.pushButtonIliValidatorCharger.clicked.connect(self.chargerIliValidator)
        self.dockwidget.pushButtonIliValidatorEffacer.clicked.connect(self.toutEffacer)
        self.dockwidget.pushButtonIliValidatorAide.clicked.connect(self.aideIliValidator)
        self.dockwidget.pushButtonCheckerCharger.clicked.connect(self.chargerChecker)
        self.dockwidget.pushButtonCheckerEffacer.clicked.connect(self.toutEffacer)
        self.dockwidget.pushButtonCheckerAide.clicked.connect(self.aideChecker)
        self.dockwidget.pushButtonVerifCharger.clicked.connect(self.chargerVerif)
        self.dockwidget.pushButtonVerifEffacer.clicked.connect(self.toutEffacer)
        self.dockwidget.pushButtonVerifAide.clicked.connect(self.aideVerif)