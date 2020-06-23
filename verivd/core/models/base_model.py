# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VeriVD plugin
 Copyright (C) 2019 Denis Rouzaud
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

from qgis.gui import QgisInterface

from verivd.core.layer_info import LayerInfo
from verivd.core.veri_meta_layer import VeriMetaLayer
from verivd.core.symbolgy_type import SymbologyType
from verivd.core.layer_list_model import LayerListModel


BASE_LAYER_INFOS = {
    "Base-Biens_fonds": (
        LayerInfo(display_name='Numéros des DDP', layer_name='006_ITF_BF_Pos_DDP'),
        LayerInfo(display_name='Numéros des biens fonds', layer_name='006_ITF_BF_Pos_Bien_fonds'),
        LayerInfo(display_name='Point limite', layer_name='006_ITF_BF_Point_limite'),
        LayerInfo(display_name='DDP', layer_name='006_ITF_BF_DDP'),
        LayerInfo(display_name='Biens fonds', layer_name='006_ITF_BF_Bien_fonds')
    ),
    "Base-Couverture_du_sol": (
        LayerInfo(display_name='Nom et numéro CS', layer_name='002_ITF_CS_Pos_Surface_CS'),
        LayerInfo(display_name='Point particulier CS', layer_name='002_ITF_CS_Point_particulier'),
        LayerInfo(display_name='Surface CS', layer_name='002_ITF_CS_Surface_CS'),
        LayerInfo(
            display_name='Bâtiment', layer_name='002_ITF_CS_Surface_CS',
            sql_request='"type" = "batiment"', symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 210, 210', 'border_color': 'black'}
        )
    ),
    "Base-Objets_divers": (
        LayerInfo(display_name='OD linéaire', layer_name='003_ITF_OD_Element_lineaire'),
        LayerInfo(display_name='OD surfacique', layer_name='003_ITF_OD_Element_surfacique'),
        LayerInfo(display_name='OD point particulier', layer_name='003_ITF_OD_Point_particulier'),
        LayerInfo(display_name='OD Nom et Numéro ligne', layer_name='003_ITF_OD_Pos_Element_lineaire'),
        LayerInfo(display_name='OD Nom et Numéro surface', layer_name='003_ITF_OD_Pos_Element_surfacique')
    ),
    "Base-Nomenclature": (
        LayerInfo(display_name='Lieux dits texte', layer_name='005_itf_no_pos_lieudit'),
        LayerInfo(display_name='Nom local texte', layer_name='005_itf_no_posnom_local'),
        LayerInfo(display_name='Nom local', layer_name='005_ITF_NO_Nom_local',
                  symbology_type=SymbologyType.RANDOM_CATEGORIZED, category_field='name')
    ),
    "Base-Conduite": (
        LayerInfo(display_name='CO Conduite', layer_name='007_itf_co_element_conduite'),
        LayerInfo(display_name='CO Conduite Nom', layer_name='007_itf_co_poselement_conduite')
    ),
    "Base-Points_fixes": [
        LayerInfo(display_name='PFP-PFA3', layer_name='001_itf_pf_points_fixes')
    ],
    "Base-Altimetrie": [
        LayerInfo(display_name='Courbes de niveau', layer_name='004_itf_al_courbes_de_niveau')
    ],
    "Base-Repartition_des_plans": [
        LayerInfo(display_name='Plan', layer_name='105_itf_rp')
    ],
    "Base-Adresses_des_batiments": (
        LayerInfo(display_name="Numéro d'entrée", layer_name='009_itf_bat_posentree_batiment'),
        LayerInfo(display_name='Nom de localisation', layer_name='009_itf_bat_posnom_localisation'),
        LayerInfo(display_name='Point de départ des tronçons', layer_name='009_itf_bat_point_depart'),
        LayerInfo(display_name='Entrée des bâtiments', layer_name='009_itf_bat_entree_batiment'),
        LayerInfo(display_name='Tronçon de rue', layer_name='009_itf_bat_troncon_rue')
    ),
    "Base-Limites_territoriales": (
        LayerInfo(display_name='Point limite territoriale',layer_name='008_itf_lt_point_limite_ter'),
        LayerInfo(display_name='Limite commune', layer_name='008_itf_lt_limite_commune'),
        LayerInfo(display_name='Autre limite', layer_name='008_itf_lt_autre_limite')
    ),
    "Base-Tous_les_topics": (
        LayerInfo(display_name='Nom et numéro CS', layer_name='002_ITF_CS_Pos_Surface_CS'),
        LayerInfo(display_name='Numéros des DDP', layer_name='006_ITF_BF_Pos_DDP'),
        LayerInfo(display_name='Numéros des biens fonds', layer_name='006_ITF_BF_Pos_Bien_fonds'),
        LayerInfo(display_name='CO Conduite Nom', layer_name='007_itf_co_poselement_conduite'),
        LayerInfo(display_name="Numéro d'entrée", layer_name='009_itf_bat_posentree_batiment'),
        LayerInfo(display_name='OD Nom et Numéro ligne', layer_name='003_ITF_OD_Pos_Element_lineaire'),
        LayerInfo(display_name='OD Nom et Numéro surface', layer_name='003_ITF_OD_Pos_Element_surfacique'),
        LayerInfo(display_name='Nom de localisation', layer_name='009_itf_bat_posnom_localisation'),
        LayerInfo(display_name='Lieux dits texte', layer_name='005_itf_no_pos_lieudit'),
        LayerInfo(display_name='Nom local texte', layer_name='005_itf_no_posnom_local'),
        LayerInfo(
            display_name='Nom local',
            layer_name='005_ITF_NO_Nom_local',
            symbology_type=SymbologyType.RANDOM_CATEGORIZED,
            category_field='name',
            opacity=.5,
            visibility=False),
        LayerInfo(display_name='PFP-PFA3', layer_name='001_itf_pf_points_fixes'),
        LayerInfo(display_name='Point limite', layer_name='006_ITF_BF_Point_limite'),
        LayerInfo(display_name='Point particulier CS', layer_name='002_ITF_CS_Point_particulier'),
        LayerInfo(display_name='Point limite térritoriale', layer_name='008_itf_lt_point_limite_ter'),
        LayerInfo(display_name='OD linéaire', layer_name='003_ITF_OD_Element_lineaire'),
        LayerInfo(display_name='OD surfacique', layer_name='003_ITF_OD_Element_surfacique'),
        LayerInfo(display_name='OD point particulier', layer_name='003_ITF_OD_Point_particulier'),
        LayerInfo(display_name='Point de départ des tronçons', layer_name='009_itf_bat_point_depart'),
        LayerInfo(display_name='Entrée des bâtiments', layer_name='009_itf_bat_entree_batiment'),
        LayerInfo(display_name='Tronçon de rue', layer_name='009_itf_bat_troncon_rue'),
        LayerInfo(display_name='CO Conduite', layer_name='007_itf_co_element_conduite'),
        LayerInfo(display_name='Courbes de niveau', layer_name='004_itf_al_courbes_de_niveau', visibility=False),
        LayerInfo(display_name='Plan', layer_name='105_itf_rp'),
        LayerInfo(display_name='Limite commune', layer_name='008_itf_lt_limite_commune'),
        LayerInfo(display_name='Autre limite', layer_name='008_itf_lt_autre_limite'),
        LayerInfo(display_name='DDP', layer_name='006_ITF_BF_DDP'),
        LayerInfo(display_name='Biens fonds', layer_name='006_ITF_BF_Bien_fonds'),
        LayerInfo(display_name='Surface CS', layer_name='002_ITF_CS_Surface_CS')
    )
}


class BaseLayerModel(LayerListModel):
    def __init__(self, iface: QgisInterface):
        layers = (
            VeriMetaLayer("Base-Tous_les_topics", "Base - Tous les topics"),
            VeriMetaLayer("Base-Points_fixes", "Base - Points fixes"),
            VeriMetaLayer("Base-Couverture_du_sol", "Base - Couverture du sol"),
            VeriMetaLayer("Base-Objets_divers", "Base - Objets divers"),
            VeriMetaLayer("Base-Altimetrie", "Base - Altimétrie"),
            VeriMetaLayer("Base-Nomenclature", "Base - Nomenclature"),
            VeriMetaLayer("Base-Biens_fonds", "Base - Biens fonds"),
            VeriMetaLayer("Base-Conduite", "Base - Conduite"),
            VeriMetaLayer("Base-Limites_territoriales", "Base - Limites territoriales"),
            VeriMetaLayer("Base-Adresses_des_batiments", "Base - Adresses des bâtiments"),
            VeriMetaLayer("Base-Repartition_des_plans", "Base - Répartition des plans"),
        )
        super(BaseLayerModel, self).__init__(iface, layers)

    def layer_infos(self, layer: str) -> [LayerInfo]:
        return BASE_LAYER_INFOS[layer]

