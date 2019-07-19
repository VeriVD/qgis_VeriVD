#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QColor
from qgis.core import QgsSymbolLayer, QgsProperty
from verivd.spatialite import SpatialiteData, LayerInfo, SymbologyType

# display_name, layerName, sqlRequest, symb, trans, visib


class BaseBiens_fonds(SpatialiteData):
    """Class used to load ownership's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Biens fonds"
        self.layer_infos = (
            LayerInfo(
                display_name='Numéros des DDP',
                layer_name='006_ITF_BF_Pos_DDP',
                symbology_type=SymbologyType.QML
            ),
            LayerInfo(
                display_name='Numéros des biens fonds',
                layer_name='006_ITF_BF_Pos_Bien_fonds',
                symbology_type=SymbologyType.QML
            ),
            LayerInfo(
                display_name='Point limite',
                layer_name='006_ITF_BF_Point_limite',
                symbology_type=SymbologyType.QML
            ),
            LayerInfo(
                display_name='DDP',
                layer_name='006_ITF_BF_Point_limite',
                symbology_type=SymbologyType.QML
            ),
            LayerInfo(
                display_name='Biens fonds',
                layer_name='006_ITF_BF_Bien_fonds',
                symbology_type=SymbologyType.QML
            )
        )


class BaseCouverture_du_sol(SpatialiteData):
    """Class used to load land cover's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Couverture du sol"
        self.layer_infos = (
            LayerInfo(
                display_name='Nom et numéro CS',
                layer_name='002_ITF_CS_Pos_Surface_CS',
                symbology_type=SymbologyType.QML
            ),
            LayerInfo(
                display_name='Point particulier CS',
                layer_name='002_ITF_CS_Point_particulier',
                symbology_type=SymbologyType.QML
            ),
            LayerInfo(
                display_name='Surface CS',
                layer_name='002_ITF_CS_Surface_CS',
                symbology_type=SymbologyType.QML
            ),
            LayerInfo(
                display_name='Bâtiment',
                layer_name='002_ITF_CS_Surface_CS',
                symbology_type=SymbologyType.SIMPLE,
                symbology_properties={
                    QgsSymbolLayer.PropertyFillColor: QgsProperty.fromValue(QColor(255, 210, 210)),
                    QgsSymbolLayer.PropertyStrokeColor: QgsProperty.fromValue(QColor(Qt.black))}
            )
        )


class BaseObjets_divers(SpatialiteData):
    """Class used to load single object's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Objets divers"
        self.layer_infos = (
            ['OD linéaire', '003_ITF_OD_Element_lineaire', '', ['qml'], '', ''],
            ['OD surfacique', '003_ITF_OD_Element_surfacique', '', [
                'qml'], '', ''],
            ["OD point particulier", '003_ITF_OD_Point_particulier', '', ['qml'], '', ''],
            ["OD Nom et Numéro ligne",
                '003_ITF_OD_Pos_Element_lineaire', '', ['qml'], '', ''],
            ["OD Nom et Numéro surface",
                '003_ITF_OD_Pos_Element_surfacique', '', ['qml'], '', '']
        )


class BaseNomenclature(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Nomenclature"
        self.layer_infos = (
            ['Lieux dits texte', '005_itf_no_pos_lieudit', '', ['qml'], '', ''],
            ['Nom local texte', '005_itf_no_posnom_local', '', ['qml'], '', ''],
            ['Nom local', '005_ITF_NO_Nom_local', '', ['randomCategorized', {'field': 'name'}], '', '']
        )


class BaseConduite(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Conduite"
        self.layer_infos = (
            ['CO Conduite', '007_itf_co_element_conduite', '', ['qml'], '', ''],
            ['CO Conduite Nom', '007_itf_co_poselement_conduite', '', ['qml'], '', '']
        )


class BasePoints_fixes(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        self.group_name = "Base - Points fixes"
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.layer_infos = [
            ['PFP-PFA3', '001_itf_pf_points_fixes', '', ['qml'], '', ''],
        ]


class BaseAltimetrie(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        self.group_name = "Base - Courbes de nivea"
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.layer_infos = [
            ['Courbes de nivea', '004_itf_al_courbes_de_nivea', '', ['qml'], '', '']
        ]


class BaseRepartition_des_plans(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        self.group_name = "Base - Répartition des plans"
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.layer_infos = [
            ['Plan', '105_itf_rp', '', ['qml'], '', '']
        ]


class BaseAdresses_des_batiments(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Adresses des bâtiments"
        self.layer_infos = (
            ["Numéro d'entrée", '009_itf_bat_posentree_batiment', '', ['qml'], '', ''],
            ['Nom de localisation', '009_itf_bat_posnom_localisation', '', ['qml'], '', ''],
            ['Point de départ des tronçons', '009_itf_bat_point_depart', '', ['qml'], '', ''],
            ['Entrée des bâtiments', '009_itf_bat_entree_batiment', '', ['qml'], '', ''],
            ['Tronçon de rue', '009_itf_bat_troncon_rue', '', ['qml'], '', '']
        )


class BaseLimites_territoriales(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Limites térritoriales"
        self.layer_infos = (
            ["Point limite térritoriale",'008_itf_lt_point_limite_ter', '', ['qml'], '', ''],
            ['Limite commune', '008_itf_lt_limite_commune', '', ['qml'], '', ''],
            ['Autre limite', '008_itf_lt_autre_limite', '', ['qml'], '', ''],
        )


class BaseTous_les_topics(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Tous les topics"
        self.layer_infos = (
            ['Nom et numéro CS', '002_ITF_CS_Pos_Surface_CS', '', ['qml'], '', ''],
            ['Numéros des DDP', '006_ITF_BF_Pos_DDP', '', ['qml'], '', ''],
            ['Numéros des biens fonds', '006_ITF_BF_Pos_Bien_fonds', '', ['qml'], '', ''],
            ['CO Conduite Nom', '007_itf_co_poselement_conduite', '', ['qml'], '', ''],
            ["Numéro d'entrée", '009_itf_bat_posentree_batiment', '', ['qml'], '', ''],
            ["OD Nom et Numéro ligne", '003_ITF_OD_Pos_Element_lineaire', '', ['qml'], '', ''],
            ["OD Nom et Numéro surface",'003_ITF_OD_Pos_Element_surfacique', '', ['qml'], '', ''],
            ['Nom de localisation', '009_itf_bat_posnom_localisation', '', ['qml'], '', ''],
            ['Lieux dits texte', '005_itf_no_pos_lieudit', '', ['qml'], '', ''],
            ['Nom local texte', '005_itf_no_posnom_local', '', ['qml'], '', ''],
            ['Nom local', '005_ITF_NO_Nom_local', '', ['randomCategorized', {'field': 'name'}], 50, 'no'],
            ['PFP-PFA3', '001_itf_pf_points_fixes', '', ['qml'], '', ''],
            ['Point limite', '006_ITF_BF_Point_limite', '', ['qml'], '', ''],
            ["Point particulier CS", '002_ITF_CS_Point_particulier', '', ['qml'], '', ''],
            ["Point limite térritoriale", '008_itf_lt_point_limite_ter', '', ['qml'], '', ''],
            ['OD linéaire', '003_ITF_OD_Element_lineaire', '', ['qml'], '', ''],
            ['OD surfacique', '003_ITF_OD_Element_surfacique', '', ['qml'], '', ''],
            ["OD point particulier", '003_ITF_OD_Point_particulier', '', ['qml'], '', ''],
            ['Point de départ des tronçons', '009_itf_bat_point_depart', '', ['qml'], '', ''],
            ['Entrée des bâtiments', '009_itf_bat_entree_batiment', '', ['qml'], '', ''],
            ['Tronçon de rue', '009_itf_bat_troncon_rue', '', ['qml'], '', ''],
            ['CO Conduite', '007_itf_co_element_conduite', '', ['qml'], '', ''],
            ['Courbes de nivea', '004_itf_al_courbes_de_nivea', '', ['qml'], '', 'no'],
            ['Plan', '105_itf_rp', '', ['qml'], '', ''],
            ['Limite commune', '008_itf_lt_limite_commune', '', ['qml'], '', ''],
            ['Autre limite', '008_itf_lt_autre_limite', '', ['qml'], '', ''],
            ["DDP", '006_ITF_BF_DDP', '', ['qml'], '', ''],
            ['Biens fonds', '006_ITF_BF_Bien_fonds', '', ['qml'], '', ''],
            ['Surface CS', '002_ITF_CS_Surface_CS', '', ['qml'], '', ''],
        )
