#!/usr/bin/env python
# -*- coding: utf-8 -*-

from verivd.core.spatialite_data import SpatialiteData
from verivd.core.symbolgy_type import SymbologyType
from verivd.core.layer_info import LayerInfo


class BaseBiens_fonds(SpatialiteData):
    """Class used to load ownership's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Biens fonds"
        self.layer_infos = (
            LayerInfo(
                display_name='Numéros des DDP',
                layer_name='006_ITF_BF_Pos_DDP',
            ),
            LayerInfo(
                display_name='Numéros des biens fonds',
                layer_name='006_ITF_BF_Pos_Bien_fonds',
            ),
            LayerInfo(
                display_name='Point limite',
                layer_name='006_ITF_BF_Point_limite',
            ),
            LayerInfo(
                display_name='DDP',
                layer_name='006_ITF_BF_DDP',
            ),
            LayerInfo(
                display_name='Biens fonds',
                layer_name='006_ITF_BF_Bien_fonds',
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
            ),
            LayerInfo(
                display_name='Point particulier CS',
                layer_name='002_ITF_CS_Point_particulier',
            ),
            LayerInfo(
                display_name='Surface CS',
                layer_name='002_ITF_CS_Surface_CS',
            ),
            LayerInfo(
                display_name='Bâtiment',
                layer_name='002_ITF_CS_Surface_CS',
				sql_request='"type" = "batiment"',
                symbology_type=SymbologyType.SIMPLE,
                symbology_properties={
                    'color': '255, 210, 210',
                    'border_color': 'black'
                }
            )
        )


class BaseObjets_divers(SpatialiteData):
    """Class used to load single object's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Objets divers"
        self.layer_infos = (
            LayerInfo(
                display_name='OD linéaire',
                layer_name='003_ITF_OD_Element_lineaire',
            ),
            LayerInfo(
                display_name='OD surfacique',
                layer_name='003_ITF_OD_Element_surfacique',
            ),
            LayerInfo(
                display_name='OD point particulier',
                layer_name='003_ITF_OD_Point_particulier',
            ),
            LayerInfo(
                display_name='OD Nom et Numéro ligne',
                layer_name='003_ITF_OD_Pos_Element_lineaire',
            ),
            LayerInfo(
                display_name='OD Nom et Numéro surface',
                layer_name='003_ITF_OD_Pos_Element_surfacique',
            )
        )


class BaseNomenclature(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Nomenclature"
        self.layer_infos = (
            LayerInfo(
                display_name='Lieux dits texte',
                layer_name='005_itf_no_pos_lieudit',
            ),
            LayerInfo(
                display_name='Nom local texte',
                layer_name='005_itf_no_posnom_local',
            ),
            LayerInfo(
                display_name='Nom local',
                layer_name='005_ITF_NO_Nom_local',
                symbology_type=SymbologyType.RANDOM_CATEGORIZED,
                category_field='name'
            )
        )


class BaseConduite(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Conduite"
        self.layer_infos = (
            LayerInfo(
                display_name='CO Conduite',
                layer_name='007_itf_co_element_conduite',
            ),
            LayerInfo(
                display_name='CO Conduite Nom',
                layer_name='007_itf_co_poselement_conduite',
            )
        )


class BasePoints_fixes(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        self.group_name = "Base - Points fixes"
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.layer_infos = [
            LayerInfo(
                display_name='PFP-PFA3',
                layer_name='001_itf_pf_points_fixes',
            )
        ]


class BaseAltimetrie(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        self.group_name = "Base - Courbes de nivea"
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.layer_infos = [
            LayerInfo(
                display_name='Courbes de niveau',
                layer_name='004_itf_al_courbes_de_niveau',
            )
        ]


class BaseRepartition_des_plans(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        self.group_name = "Base - Répartition des plans"
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.layer_infos = [
            LayerInfo(
                display_name='Plan',
                layer_name='105_itf_rp',
            )
        ]


class BaseAdresses_des_batiments(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Adresses des bâtiments"
        self.layer_infos = (
            LayerInfo(
                display_name="Numéro d'entrée",
                layer_name='009_itf_bat_posentree_batiment',
            ),
            LayerInfo(
                display_name='Nom de localisation',
                layer_name='009_itf_bat_posnom_localisation',
            ),
            LayerInfo(
                display_name='Point de départ des tronçons',
                layer_name='009_itf_bat_point_depart',
            ),
            LayerInfo(
                display_name='Entrée des bâtiments',
                layer_name='009_itf_bat_entree_batiment',
            ),
            LayerInfo(
                display_name='Tronçon de rue',
                layer_name='009_itf_bat_troncon_rue',
            )
        )


class BaseLimites_territoriales(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Limites térritoriales"
        self.layer_infos = (
            LayerInfo(
                display_name='Point limite térritoriale',
                layer_name='008_itf_lt_point_limite_ter',
            ),
            LayerInfo(
                display_name='Limite commune',
                layer_name='008_itf_lt_limite_commune',
            ),
            LayerInfo(
                display_name='Autre limite',
                layer_name='008_itf_lt_autre_limite',
            )
        )


class BaseTous_les_topics(SpatialiteData):
    """Class used to load local names's layers"""

    def __init__(self, iface, pathSQliteDB):
        SpatialiteData.__init__(self, iface, pathSQliteDB)
        self.group_name = "Base - Tous les topics"
        self.layer_infos = (
            LayerInfo(
                display_name='Nom et numéro CS',
                layer_name='002_ITF_CS_Pos_Surface_CS',
            ),
            LayerInfo(
                display_name='Numéros des DDP',
                layer_name='006_ITF_BF_Pos_DDP',
            ),
            LayerInfo(
                display_name='Numéros des biens fonds',
                layer_name='006_ITF_BF_Pos_Bien_fonds',
            ),
            LayerInfo(
                display_name='CO Conduite Nom',
                layer_name='007_itf_co_poselement_conduite',
            ),
            LayerInfo(
                display_name="Numéro d'entrée",
                layer_name='009_itf_bat_posentree_batiment',
            ),
            LayerInfo(
                display_name='OD Nom et Numéro ligne',
                layer_name='003_ITF_OD_Pos_Element_lineaire',
            ),
            LayerInfo(
                display_name='OD Nom et Numéro surface',
                layer_name='003_ITF_OD_Pos_Element_surfacique',
            ),
            LayerInfo(
                display_name='Nom de localisation',
                layer_name='009_itf_bat_posnom_localisation',
            ),
            LayerInfo(
                display_name='Lieux dits texte',
                layer_name='005_itf_no_pos_lieudit',
            ),
            LayerInfo(
                display_name='Nom local texte',
                layer_name='005_itf_no_posnom_local',
            ),
            LayerInfo(
                display_name='Nom local',
                layer_name='005_ITF_NO_Nom_local',
                symbology_type=SymbologyType.RANDOM_CATEGORIZED,
                category_field='name',
                opacity=.5,
                visibility=False
            ),
            LayerInfo(
                display_name='PFP-PFA3',
                layer_name='001_itf_pf_points_fixes',
            ),
            LayerInfo(
                display_name='Point limite',
                layer_name='006_ITF_BF_Point_limite',
            ),
            LayerInfo(
                display_name='Point particulier CS',
                layer_name='002_ITF_CS_Point_particulier',
            ),
            LayerInfo(
                display_name='Point limite térritoriale',
                layer_name='008_itf_lt_point_limite_ter',
            ),
            LayerInfo(
                display_name='OD linéaire',
                layer_name='003_ITF_OD_Element_lineaire',
            ),
            LayerInfo(display_name='OD surfacique', layer_name='003_ITF_OD_Element_surfacique'),
            LayerInfo(display_name='OD point particulier', layer_name='003_ITF_OD_Point_particulier'),
            LayerInfo(display_name='Point de départ des tronçons', layer_name='009_itf_bat_point_depart'),
            LayerInfo(display_name='Entrée des bâtiments', layer_name='009_itf_bat_entree_batiment'),
            LayerInfo(display_name='Tronçon de rue', layer_name='009_itf_bat_troncon_rue'),
            LayerInfo(display_name='CO Conduite', layer_name='007_itf_co_element_conduite'),
            LayerInfo(display_name='Courbes de nivea', layer_name='004_itf_al_courbes_de_nivea', visibility=False),
            LayerInfo(display_name='Plan', layer_name='105_itf_rp'),
            LayerInfo(display_name='Limite commune', layer_name='008_itf_lt_limite_commune'),
            LayerInfo(display_name='Autre limite', layer_name='008_itf_lt_autre_limite'),
            LayerInfo(display_name='DDP', layer_name='006_ITF_BF_DDP'),
            LayerInfo(display_name='Biens fonds', layer_name='006_ITF_BF_Bien_fonds'),
            LayerInfo(display_name='Surface CS', layer_name='002_ITF_CS_Surface_CS'),
        )
