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

from qgis.PyQt.QtCore import Qt

from qgis.core import QgsSymbolLayer, QgsProperty
from qgis.gui import QgisInterface

from verivd.core.symbolgy_type import SymbologyType
from verivd.core.layer_info import LayerInfo
from verivd.core.layer_list_model import LayerListModel
from verivd.core.veri_meta_layer import VeriMetaLayer


VERIF_LAYER_INFOS = {
    "VerifBiens_fonds": (
        LayerInfo(display_name="Point limite non-matérialisé, vérification de l'attribut \"defini_exactement\"", layer_name='122_verif_BF_PL_non_mat_def_exa', control_layer=True),
        LayerInfo(display_name='Sommet manquant sous un point limite', layer_name='100_verif_bf_sommet_manquant_sous_pl', control_layer=True),
        LayerInfo(display_name='Sommet proche d\'une limite', layer_name='100_verif_bf_sommet_proche_pl', control_layer=True),
        LayerInfo(display_name='Point limite manquant sur un sommet', layer_name='100_verif_bf_pl_manquant_sur_sommet', control_layer=True),
        LayerInfo(display_name='Point limite isolé', layer_name='100_verif_bf_pl_isole', control_layer=True),
        LayerInfo(display_name='Point limite avant point', layer_name='100_verif_bf_pl_avant_point', control_layer=True),
        LayerInfo(display_name='Point limite hors périmètre', layer_name='100_verif_bf_pl_hors_perimetre'),
        LayerInfo(display_name='Point limite en bordure du périmètre', layer_name='100_verif_bf_pl_sur_bord_perimetre', control_layer=True),
        LayerInfo(display_name='Point limite décrivant une limite quasi-alignée',layer_name='101_verif_bf_pl_aligne', control_layer=True),
        LayerInfo(display_name='Ecart d\'alignement', layer_name='101_verif_bf_distance_alignement'),
        LayerInfo(display_name='Segment de biens fonds simplifié', layer_name='101_verif_bf_segment_bf_modifie'),
        LayerInfo(display_name='Segment de DDP simplifié', layer_name='101_verif_ddp_segment_bf_modifie'),
        LayerInfo(display_name='Précision planimétrique des points limites', layer_name='100_verif_bf_pl_precplannum'),
        LayerInfo(display_name='Point limite', layer_name='006_ITF_BF_Point_limite'),
        LayerInfo(display_name='Numéros des biens fonds', layer_name='006_ITF_BF_Pos_Bien_fonds'),
        LayerInfo(display_name='Numéros des DDP', layer_name='006_ITF_BF_Pos_DDP'),
        LayerInfo(display_name='DDP', layer_name='006_ITF_BF_DDP'),
        LayerInfo(display_name='Biens fonds', layer_name='006_ITF_BF_Bien_fonds'),
        LayerInfo(display_name='Biens fonds à proximité du lot', layer_name='111_bdmo_biens_fonds_alentours'),
        LayerInfo(display_name='Différence des surfaces des immeubles selon 6422bis', layer_name='107_verif_6422bis', visibility=False),
        LayerInfo(display_name='Plans en vigueur à proximité du lot', layer_name='111_bdmo_repartition_plans_alentours'),
        LayerInfo(display_name='Plans en vigueur du lot', layer_name='111_bdmo_repartition_plan_en_vigueur_du_lot')
    ),
    "VerifNomenclature": (
        LayerInfo(
            display_name='point divergent entre les immeubles et la nomenclature', layer_name='103_VERIF_BF_NO_Point',
            symbology_type=SymbologyType.SIMPLE, symbology_properties={'color': '255, 255, 0', 'size': '4'},
            control_layer=True
        ),
        LayerInfo(
            display_name='Sifflet entre les immeubles et la nomenclature', layer_name='103_VERIF_BF_NO_Surface',
            symbology_type=SymbologyType.SIMPLE, symbology_properties={'color': '255, 0, 0'},
            control_layer=True
        ),
        LayerInfo(display_name='Lieux dits texte', layer_name='005_itf_no_pos_lieudit'),
        LayerInfo(display_name='Nom local texte', layer_name='005_itf_no_posnom_local'),
        LayerInfo(display_name='Plan', layer_name='105_itf_rp'),
        LayerInfo(
            display_name='Nom local', layer_name='005_ITF_NO_Nom_local',
            symbology_type=SymbologyType.RANDOM_CATEGORIZED, category_field='name', opacity=0.5
        ),
        LayerInfo(display_name='DDP', layer_name='006_ITF_BF_DDP'),
        LayerInfo(display_name='Biens fonds', layer_name='006_ITF_BF_Bien_fonds')
    ),
    "VerifAdresses": (
        LayerInfo(display_name='Numéro d\'entrée', layer_name='009_itf_bat_posentree_batiment', control_layer=True),
        LayerInfo(display_name='Point de départ des tronçons', layer_name='009_itf_bat_point_depart', control_layer=True),
        LayerInfo(display_name='Entrée des bâtiments', layer_name='009_itf_bat_entree_batiment', control_layer=True),
        LayerInfo(display_name='Entrée du RCB', layer_name='104_dwh_adresse_rcb', visibility=False, control_layer=True),
        LayerInfo(display_name='Différence avec les entrées du RCB', layer_name='104_verif_entreemo_diff_rcb', visibility=False, control_layer=True),
        LayerInfo(display_name='Lien entre les entrées et les localisations', layer_name='109_VERIF_Entree_Vers_Localisation', control_layer=True),
        LayerInfo(display_name='Sens du tronçon', layer_name='009_ITF_BAT_Troncon_rue', control_layer=True),
        LayerInfo(
            display_name='Nom des rues', layer_name='009_ITF_BAT_Troncon_rue',
            symbology_type=SymbologyType.RANDOM_CATEGORIZED, category_field='texte',
            symbology_data_defined_properties={
                QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(3),
                QgsSymbolLayer.PropertyCapStyle: QgsProperty.fromValue(Qt.RoundCap),
                QgsSymbolLayer.PropertyJoinStyle: QgsProperty.fromValue(Qt.RoundJoin),
            },
            control_layer=True
        ),
        LayerInfo(display_name='Lieu dénommé', layer_name='009_ITF_BAT_Lieu_denomme'),
        LayerInfo(
            display_name='Habitation sans adresse',
            layer_name='108_VERIF_Habitation_sans_adresse',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 0, 0, 180','border_color': '255, 255, 0'},
            visibility=False
        ),
        LayerInfo(
            display_name='Bâtiment et surface en dur',
            layer_name='002_ITF_CS_Surface_CS',
            sql_request='"type" = "batiment" OR "vd_genre" LIKE "revetement_dur%"'
        ),
        LayerInfo(
            display_name='DP',
            layer_name='006_ITF_BF_Bien_fonds',
            sql_request='"number" LIKE "DP%"',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={
                'color': '255, 255, 255',
                'border_color': '0,0,0',
                'width_border': '0.5'
            }
        ),
        LayerInfo(display_name='Couverture du sol', layer_name='002_ITF_CS_Surface_CS', opacity=.5)
    ),
    "VerifCouverture_du_sol_et_objets_divers":	(

        LayerInfo(
            display_name='OD - devrait être entouré par un objet surfacique',
            layer_name='114_verif_od_surflineaire_sanssurf',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 100, 0', 'width': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='OD - Elément  surfacique qui devrait être linéaire',
            layer_name='114_VERIF_OD_surfaciqueErreur',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 0, 0', 'width': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='OD - Elément linéaire qui devrait être surfacique',
            layer_name='114_VERIF_OD_lineaireErreur',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 0, 0', 'width': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='Point particulier CS manquant sous un angle de bâtiment',
            layer_name='113_cs_pointbatiment',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 100, 200', 'size': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='Validation OGC des objets divers',
            layer_name='110_od_ogc_geometrie',
            symbology_type=SymbologyType.RANDOM_CATEGORIZED,
            category_field='issue_found',
            symbology_data_defined_properties={QgsSymbolLayer.PropertySize: QgsProperty.fromValue(2)},
            control_layer=True
        ),
        LayerInfo(
            display_name='point divergent entre les immeubles et la couverture du sol',
            layer_name='103_verif_bf_cs_point',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 255, 0', 'size': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='Sifflet entre les immeubles et la couverture du sol',
            layer_name='103_verif_bf_cs_surface',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 0, 0'},
            control_layer=True
        ),
        LayerInfo(display_name='Nombre de géométrie par objet divers linéaires', layer_name='102_verif_od_lineaire_fid', control_layer=True),
        LayerInfo(display_name='Nombre de géométrie par objet divers surfacique', layer_name='102_verif_od_surfacique_fid', control_layer=True),
        LayerInfo(
            display_name='Objets divers linéaires (relation vers les géométries)',
            layer_name='102_verif_od_lineaire_fid', symbology_type=SymbologyType.RANDOM_CATEGORIZED,
            category_field='fid_od',
            symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(3)},
            opacity=.5,
            control_layer=True
        ),
        LayerInfo(
            display_name='Objets divers surfaciques (relation vers les géométries)',
            layer_name='102_verif_od_surfacique_fid',
            symbology_type=SymbologyType.RANDOM_CATEGORIZED,
            category_field='fid_od',
            symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(0.5)},
            opacity=.5,
            control_layer=True
        ),

        LayerInfo(display_name='Point particulier pas sur sommet (vecteur de la couche correspondante)',layer_name='126_verif_point_cs_od',control_layer=True),
        LayerInfo(display_name='CS - Point particulier de bâtiment proche limite BF (vecteur)',layer_name='120_verif_CS_Point_sit_proche_BF_Vecteur',control_layer=True),
        LayerInfo(display_name='CS - Point particulier de bâtiment proche limite BF',layer_name='120_verif_CS_Point_sit_proche_BF',control_layer=True),
        LayerInfo(display_name='OD - Incohérence entre le genre et la désignation',layer_name='121_verif_OD_test_designation',control_layer=True),
        LayerInfo(display_name='OD linéaire', layer_name='003_ITF_OD_Element_lineaire'),
        LayerInfo(display_name='OD surfacique', layer_name='003_ITF_OD_Element_surfacique'),
        LayerInfo(display_name='OD point particulier', layer_name='003_ITF_OD_Point_particulier'),
        LayerInfo(display_name='OD Nom et Numéro ligne', layer_name='003_ITF_OD_Pos_Element_lineaire'),
        LayerInfo(display_name='OD Nom et Numéro surface', layer_name='003_ITF_OD_Pos_Element_surfacique'),
        LayerInfo(display_name='Nom et numéro CS', layer_name='002_ITF_CS_Pos_Surface_CS'),
        LayerInfo(display_name='Point particulier CS', layer_name='002_ITF_CS_Point_particulier'),
        LayerInfo(
            display_name='Bâtiment',
            layer_name='002_ITF_CS_Surface_CS',
            sql_request='"type" = "batiment"',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 210, 210'}),
        LayerInfo(display_name='DDP', layer_name='006_ITF_BF_DDP'),
        LayerInfo(display_name='Biens fonds', layer_name='006_ITF_BF_Bien_fonds'),
        LayerInfo(display_name='Surface CS', layer_name='002_ITF_CS_Surface_CS', opacity=.5)
    ),
    "VerifContinuite_des_reseaux":	(
        LayerInfo(
            display_name='CS Nom et numéro',
            layer_name='002_ITF_CS_Pos_Surface_CS',
            sql_request='"type" = "Nom_objet" AND ("number_name" LIKE "Route%" OR "number_name" LIKE "Ruisseau%" OR "number_name" LIKE "La%" OR "number_name" LIKE "Le%")',
            control_layer=True
        ),
        LayerInfo(
            display_name='OD Nom et numéro', layer_name='003_ITF_OD_Pos_Element_lineaire',
            sql_request='"number_name" LIKE "Ligne%"',
            control_layer=True
        ),
        LayerInfo(display_name='Cours d\'eau (DGE)', layer_name='112_DWH_Gesreau', opacity=.5, control_layer=True),
        LayerInfo(display_name='Traversé de localité (DGMR)', layer_name='112_DWH_TraverseLocalite', control_layer=True),
        LayerInfo(display_name='Axes de maintenance du réseau routier (DGMR)', layer_name='112_dwh_axe'),
        LayerInfo(
            display_name='Couverture du sol',
            layer_name='002_ITF_CS_Surface_CS',
            sql_request='"vd_genre" IN ("eau.cours_eau", "revetement_dur.route_chemin","revetement_dur.chemin_de_fer")',
            opacity=.5,
            control_layer=True
        ),
        LayerInfo(
            display_name='Réseaux dans les objet divers linéaires',
            layer_name='003_ITF_OD_Element_lineaire',
            sql_request='"vd_genre" IN ("eau_canalisee_souterraine","tunnel_passage_inferieur_galerie","pont_passerelle","quai","ru","sentier","ligne_aerienne_a_haute_tension","mat_antenne","conduite_forcee","voie_ferree,telepherique","telecabine_telesiege","telepherique_de_chantier","skilift","bac","axe")',
            control_layer=True
        ),
        LayerInfo(
            display_name='Réseaux dans les objet divers surfaciques',
            layer_name='003_ITF_OD_Element_surfacique',
            sql_request='"vd_genre" IN ("eau_canalisee_souterraine","tunnel_passage_inferieur_galerie","pont_passerelle","quai","ru","sentier","ligne_aerienne_a_haute_tension","mat_antenne","conduite_forcee","voie_ferree,telepherique","telecabine_telesiege","telepherique_de_chantier","skilift","bac","axe")',
            control_layer=True
        ),
        LayerInfo(
            display_name='DP',
            layer_name='006_ITF_BF_Bien_fonds',
            sql_request='"number" LIKE "DP%"',
            control_layer=True
        ),
        LayerInfo(display_name='Périmetre du lot', layer_name='112_itf_mise_a_jourrp')
    ),
    "VerifPoints_fixes": (
        LayerInfo(
            display_name='Point fixes dont les attributs ITF vs BDMO ne sont pas identiques',
            layer_name='115_itf_pfp_problemeattribut',
            opacity=.5, visibility=False,
            control_layer=True
        ),
        LayerInfo(display_name='Points fixes en BDMO mais pas dans le fichier ITF', layer_name='115_bdmo_pfp_en_plus', control_layer=True),
        LayerInfo(display_name='Points fixes dans le fichier ITF mais pas en BDMO', layer_name='115_itf_pfp_en_plus', visibility=False, control_layer=True),
        LayerInfo(display_name='Points fixes dans le fichier ITF mais en dehors du lot', layer_name='115_itf_pfp_horslot', control_layer=True),
        LayerInfo(display_name='PFP-PFA3', layer_name='001_itf_pf_points_fixes'),
        LayerInfo(display_name='Précision planimétrique des points fixes', layer_name='115_itf_pfp'),
        LayerInfo(display_name='Périmetre du lot', layer_name='112_itf_mise_a_jourrp')
    ),
    "VerifLimites_territoriales_et_administratives": (
        LayerInfo(
            display_name='Géometrie de limite de canton incorrecte (OGC)',
            layer_name='116_LigneCANT_OGC_fail',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 255, 0', 'size': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='Géometrie de limite de commune incorrecte (OGC)',
            layer_name='116_LigneCOM_OGC_fail',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 255, 0', 'size': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='Géometrie de limite de district incorrecte (OGC)',
            layer_name='116_LigneDIST_OGC_fail',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 255, 0', 'size': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='point de limite territoriale manquant sur sommet de limite de commune',
            layer_name='116_PL_terr_manquant_sous_sommet_COM',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 255, 0', 'size': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='sommet de limite de commune manquant sous point de limite territoriale',
            layer_name='116_Sommet_COM_manquant_sous_PL_terr',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 255, 0', 'size': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='sommet de limite de commune manquant sous sommet de limite de canton',
            layer_name='116_sommetCOM_manquant_sous_sommet_CANT',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 255, 0', 'size': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='sommet de limite decommune manquant sous sommet de limite de district',
            layer_name='116_sommetCOM_manquant_sous_sommet_Dist',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 255, 0', 'size': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='point divergent entre les immeubles et la limite de commune',
            layer_name='103_VERIF_BF_COM_Point',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 255, 0', 'size': '2'},
            control_layer=True
        ),
        LayerInfo(
            display_name='Sifflet entre les immeubles et la limite de commune',
            layer_name='103_VERIF_BF_COM_Surface',
            symbology_type=SymbologyType.SIMPLE,
            symbology_properties={'color': '255, 0, 0'},
            control_layer=True
        ),
        LayerInfo(display_name='Point limite térritoriale', layer_name='008_itf_lt_point_limite_ter'),
        LayerInfo(display_name='Limite commune', layer_name='008_itf_lt_limite_commune'),
        LayerInfo(display_name='Autre limite', layer_name='008_itf_lt_autre_limite'),
        LayerInfo(display_name='DDP', layer_name='006_ITF_BF_DDP', opacity=.5),
        LayerInfo(display_name='Biens fonds', layer_name='006_ITF_BF_Bien_fonds', opacity=.5)
    ),
    "VerifNumerotation": (
        LayerInfo(display_name='Fléche du doublon de numéro', layer_name='123_verif_numdoublonfleche', control_layer=True),
        LayerInfo(display_name='Doublon de numéro', layer_name='123_verif_numdoublon', control_layer=True),
        LayerInfo(display_name="Numéros d'immeuble différents entre la BDMO et ITF", layer_name='123_verif_num_imm_diff_dwh_itf', control_layer=True),
        LayerInfo(display_name='IdentDN incorrect - ITF', layer_name='105_verif_point_sur_mauvais_plan', control_layer=True),
        LayerInfo(display_name='Bâtiment hors lot, sur la commune - BDMO', layer_name='123_verif_num_baths_dwh'),
        LayerInfo(display_name='Bâtment soutterrain hors lot, sur la commune - BDMO', layer_name='123_verif_num_batss_dwh'),
        LayerInfo(display_name='Bâtiment dans le lot - ITF', layer_name='002_ITF_CS_Surface_CS', sql_request='"type" = "batiment"'),
        LayerInfo(display_name='Bâtiment soutterrain dans le lot - ITF', layer_name='003_ITF_OD_Element_surfacique', sql_request='"vd_genre" = "batiment_souterrain"'),
        LayerInfo(display_name='DDP dans le lot - ITF', layer_name='006_ITF_BF_DDP'),
        LayerInfo(display_name='Parcelles dans le lot - ITF', layer_name='006_ITF_BF_Bien_fonds'),
        LayerInfo(display_name='Parcelles hors lot, sur la commune - BDMO', layer_name='123_verif_num_bf_dwh'),
        LayerInfo(display_name='Répartition des plans du lot', layer_name='105_itf_rp'),
        LayerInfo(display_name='Plans alentours', layer_name='111_bdmo_repartition_plans_alentours'),
        LayerInfo(display_name='Limite commune - BDMO', layer_name='123_verif_num_com_dwh'),
        LayerInfo(display_name='Périmetre du lot', layer_name='112_itf_mise_a_jourrp')
    ),
    "VerifGeometrie": (
        LayerInfo(
            display_name='Test OGC',
            layer_name='119_verif_geomogc',
            symbology_type=SymbologyType.RANDOM_CATEGORIZED,
            category_field='topic',
            symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(3)},
            opacity=.5,
            visibility=True,
            control_layer=True
        ),

        LayerInfo(display_name='Arc dont la flèche est inférieure à 3.5cm', layer_name='106_verif_segmentarc', sql_request='"fleche" < 0.035',visibility=True,control_layer=True),
        LayerInfo(display_name='Arc de cercle', layer_name='106_verif_segmentarc', visibility=False),
        LayerInfo(display_name="Position de label à vérifier", layer_name='125_verif_poscroisementvecteur',visibility=True,control_layer=True),
        LayerInfo(display_name="Traits de rappel", layer_name='125_verif_pos',visibility=False),
        LayerInfo(display_name="Géométrie superposée dans l'ITF", layer_name='119_verif_geomsuperpose',control_layer=True),
        LayerInfo(display_name='Coordonnée identique entre BDMO et ITF', layer_name='124_verif_coord_coordidentiqueitf_dwh',control_layer=True),
        LayerInfo(display_name='Vecteurs BDMO', layer_name='124_verif_coord_vecteur_dwh',control_layer=True),

        LayerInfo(
            display_name='Objet ponctuel hors du périmètre du lot',
            layer_name='112_itf_objet_hors_perimetrelot_point',
            symbology_type=SymbologyType.RANDOM_CATEGORIZED,
            category_field='nomtable',
            symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(3)},
            opacity=.5,
            visibility=False,
            control_layer=True
        ),
        LayerInfo(
            display_name='Objet linéaire hors du périmètre du lot',
            layer_name='112_itf_objet_hors_perimetrelot_ligne',
            symbology_type=SymbologyType.RANDOM_CATEGORIZED,
            category_field='nomtable',
            symbology_data_defined_properties={QgsSymbolLayer.PropertyWidth: QgsProperty.fromValue(2)},
            opacity=.5,
            visibility=False,
            control_layer=True
        ),
        LayerInfo(
            display_name='Objet surfacique hors du périmètre du lot',
            layer_name='112_itf_objet_hors_perimetre_surface',
            symbology_type=SymbologyType.RANDOM_CATEGORIZED,
            category_field='nomtable',
            symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
            opacity=.5,
            visibility=False,
            control_layer=True
        ),
        LayerInfo(display_name='OD linéaire', layer_name='003_ITF_OD_Element_lineaire'),
        LayerInfo(display_name='OD surfacique', layer_name='003_ITF_OD_Element_surfacique'),
        LayerInfo(display_name='DDP dans le lot - ITF', layer_name='006_ITF_BF_DDP'),
        LayerInfo(display_name='Bien fonds', layer_name='006_ITF_BF_Bien_fonds', control_layer=True),
        LayerInfo(display_name='Surface CS', layer_name='002_ITF_CS_Surface_CS'),
        LayerInfo(display_name='Périmetre du lot', layer_name='112_itf_mise_a_jourrp')
    ),
}


def create_veri_meta_layers():
    return (
        VeriMetaLayer("VerifAdresses", "Vérification - Adresses"),
        VeriMetaLayer("VerifBiens_fonds", "Vérification - Biens fonds"),
        VeriMetaLayer("VerifCouverture_du_sol_et_objets_divers", "Vérification - Couverture du sol et objets divers"),
        VeriMetaLayer("VerifContinuite_des_reseaux", "Vérification - Continuite des reseaux"),
        VeriMetaLayer("VerifGeometrie", "Vérification - Géométries"),
        VeriMetaLayer("VerifNomenclature", "Vérification - Nomenclature"),
        VeriMetaLayer("VerifNumerotation", "Vérification - Numérotation"),
        VeriMetaLayer("VerifLimites_territoriales_et_administratives", "Vérification - Limites territoriales et administratives"),
        VeriMetaLayer("VerifPoints_fixes", "Vérification - Points fixes")
    )


class VerifLayerModel(LayerListModel):
    def __init__(self, iface: QgisInterface):
        super(VerifLayerModel, self).__init__(iface, create_veri_meta_layers(), has_control_layers=True)

    def reload(self):
        self.veri_meta_layers = create_veri_meta_layers()

    def layer_infos(self, layer: str) -> [LayerInfo]:
        return VERIF_LAYER_INFOS[layer]
