#!/usr/bin/env python
# -*- coding: utf-8 -*-


from qgis.core import QgsSymbolLayer, QgsProperty
from qgis.PyQt.QtCore import Qt
from verivd.core.spatialite_data import SpatialiteData
from verivd.core.symbolgy_type import SymbologyType
from verivd.core.layer_info import LayerInfo


# display_name, layer_name, sql_request, symb, trans, visib

class VerifBiens_fonds(SpatialiteData):
	"""Class used to load test on BF's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)
		self.group_name = 'Vérification - biens fonds'
		# set layer's parameter in a dict list
		self.layer_infos = (	
			LayerInfo(display_name='Sommet manquant sous un point limite', layer_name='100_verif_bf_sommet_manquant_sous_pl'),
			LayerInfo(display_name='Sommet proche d\'une limite', layer_name='100_verif_bf_sommet_proche_pl'),
			LayerInfo(display_name='Point limite manquant sur un sommet', layer_name='100_verif_bf_pl_manquant_sur_sommet'),
			LayerInfo(display_name='Point limite isolé', layer_name='100_verif_bf_pl_isole'),
			LayerInfo(display_name='Point limite avant point', layer_name='100_verif_bf_pl_avant_point'),
			LayerInfo(display_name='Point limite hors périmètre', layer_name='100_verif_bf_pl_hors_perimetre'),
			LayerInfo(display_name='Point limite en bordure du périmètre', layer_name='100_verif_bf_pl_sur_bord_perimetre'),
			LayerInfo(display_name='Point limite décrivant une limite quasi-alignée',layer_name='101_verif_bf_pl_aligne'),
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
		)
		self.check_layer = (
			'Sommet manquant sous un point limite',
			'Sommet proche d\'une limite',
			'Point limite manquant sur un sommet',
			'Point limite isolé',
			'Point limite avant point',
			'Point limite en bordure du périmètre',
			'Point limite décrivant une limite quasi-alignée'
		)

class VerifNomenclature(SpatialiteData):
	"""Class used to load test on NO's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)
		self.group_name = 'Vérification des sifflets sur les biens fonds'
		# set layer's parameter in a dict list
		self.layer_infos = (
			LayerInfo(
				display_name='point divergent entre les immeubles et la nomenclature',
				layer_name='103_VERIF_BF_NO_Point',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 255, 0',
					'size': '4'
				}
			),
			LayerInfo(
				display_name='Sifflet entre les immeubles et la nomenclature',
				layer_name='103_VERIF_BF_NO_Surface',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={'color': '255, 0, 0'}
			),
			LayerInfo(
				display_name='Nom local',
				layer_name='005_ITF_NO_Nom_local',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='name',
				opacity=0.5
			),
			LayerInfo(display_name='DDP', layer_name='006_ITF_BF_DDP'),
			LayerInfo(display_name='Biens fonds', layer_name='006_ITF_BF_Bien_fonds')
		)
		self.check_layer = (
			'point divergent entre les immeubles et la nomenclature',
			'Sifflet entre les immeubles et la nomenclature'
		)

class VerifAdresses(SpatialiteData):
	"""Class used to load test on BAT's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)
		self.group_name = u"Vérification des adresses"
		# set layer's parameter in a dict list
		self.layer_infos = 	(	
			LayerInfo(display_name='Numéro d\'entrée', layer_name='009_itf_bat_posentree_batiment'),
			LayerInfo(display_name='Point de départ des tronçons', layer_name='009_itf_bat_point_depart'),
			LayerInfo(display_name='Entrée des bâtiments', layer_name='009_itf_bat_entree_batiment'),
			LayerInfo(display_name='Entrée du RCB', layer_name='104_dwh_adresse_rcb', visibility=False),
			LayerInfo(display_name='Différence entre les entrées de la MO et celles du RCB', layer_name='104_verif_entreemo_diff_rcb', visibility=False),
			LayerInfo(display_name='Raccord des entrées vers localisation', layer_name='109_VERIF_Entree_Vers_Localisation'),
			LayerInfo(display_name='Sens du tronçon', layer_name='009_ITF_BAT_Troncon_rue'),
			LayerInfo(
				display_name='Nom rue',
				layer_name='009_ITF_BAT_Troncon_rue',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='texte',
				symbology_data_defined_properties={
					QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(3),
					QgsSymbolLayer.PropertyCapStyle: QgsProperty.fromValue(Qt.RoundCap),
					QgsSymbolLayer.PropertyJoinStyle: QgsProperty.fromValue(Qt.RoundJoin),
				}
			),
			LayerInfo(
				display_name='Habitation sans adresses',
				layer_name='108_VERIF_Habitation_sans_adresse',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 0, 0, 180',
					'border_color': '255, 255, 0'
				},
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
			LayerInfo(
				display_name='Couverture du sol',
				layer_name='002_ITF_CS_Surface_CS',
				opacity=.5
			)
		)

		self.check_layer = (
			"Numéro d'entrée",
			'Nom rue',
			'Point de départ des tronçons',
			'Entrée des bâtiments',
			'Entrée du RCB',
			'Différence entre les entrées de la MO et celles du RCB',
			'Raccord des entrées vers localisation',
			'Sens du tronçon'
		)

class VerifCouverture_du_sol_et_objets_divers(SpatialiteData):
	"""Class used to load test on CS's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)
		self.group_name = u"Vérification de la couverture du sol et des objets divers"
		# set layer's parameter in a dict list
		self.layer_infos = 	(	
			LayerInfo(
				display_name='OD - Element surfacique qui devrait être linéaire',
				layer_name='114_VERIF_OD_surfaciqueErreur',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 0, 0',
					'width': '2'
				}
			),
			LayerInfo(
				display_name='OD - Element linéaire qui devrait être surfacique', 
				layer_name='114_VERIF_OD_lineaireErreur',
				symbology_type=SymbologyType.SIMPLE, 
				symbology_properties={
					'color': '255, 0, 0',
					'width': '2'
				}
			),
			LayerInfo(
				display_name='Point particulier CS manquant sous un angle de bâtiment', 
				layer_name='113_cs_pointbatiment', 
				symbology_type=SymbologyType.SIMPLE, 
				symbology_properties={
					'color': '255, 100, 200',
					'size': '2'
				}
			),
			LayerInfo(
				display_name='Validation OGC des objets divers',
				layer_name='110_od_ogc_geometrie',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='issue_found', 
				symbology_data_defined_properties={QgsSymbolLayer.PropertySize: QgsProperty.fromValue(2)}
			),
			LayerInfo(
				display_name='point divergent entre les immeubles et la couverture du sol', 
				layer_name='103_verif_bf_cs_point', 
				symbology_type=SymbologyType.SIMPLE, 
				symbology_properties={
					'color': '255, 255, 0',
					'size': '2'
				}
			),
			LayerInfo(
				display_name='Sifflet entre les immeubles et la couverture du sol', 
				layer_name='103_verif_bf_cs_surface', 
				symbology_type=SymbologyType.SIMPLE, 
				symbology_properties={'color': '255, 0, 0'}
			),
			LayerInfo(display_name='Nombre de géomètrie par objet divers linéaires', layer_name='102_verif_od_lineaire_fid'),
			LayerInfo(display_name='Nombre de géomètrie par objet divers surfacique', layer_name='102_verif_od_surfacique_fid'),
			LayerInfo(
				display_name='Objets divers linéaires (relation vers les géomètries)', 
				layer_name='102_verif_od_lineaire_fid', symbology_type=SymbologyType.RANDOM_CATEGORIZED, 
				category_field='fid_od',
				symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(3)},
				opacity=.5
			),
			LayerInfo(
				display_name='Objets divers surfaciques (relation vers les géomètries)',
				layer_name='102_verif_od_surfacique_fid',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED, 
				category_field='fid_od',
				symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(0.5)},
				opacity=.5
			),
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
		)

		self.check_layer = (
			'OD - Element surfacique qui devrait être linéaire',
			'OD - Element linéaire qui devrait être surfacique',
			'Point particulier CS manquant sous un angle de bâtiment',
			"Validation OGC des objets divers",
			'point divergent entre les immeubles et la couverture du sol',
			'Sifflet entre les immeubles et la couverture du sol',
			"Nombre de géomètrie par objet divers linéaires",
			"Nombre de géomètrie par objet divers surfacique",
			"Objets divers linéaires (relation vers les géomètries)",
			"Objets divers surfaciques (relation vers les géomètries)"
		)


class VerifRepartition_des_plans_et_domaine_de_numerotation(SpatialiteData):
	"""Class used to load test on RP's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)
		self.group_name = u"Vérification de la répartition des plans et de la numérotation des points"
		# set layer's parameter in a dict list
		self.layer_infos = (	
			LayerInfo(
				display_name='point divergent entre les immeubles et la répartition des plans',
				layer_name='103_VERIF_BF_RP_Point',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 255, 0',
					'size': '2'
				}
			),
			LayerInfo(
				display_name='Sifflet entre les immeubles et la répartition des plans',
				layer_name='103_VERIF_BF_RP_Surface',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={'color': '255, 0, 0'}
			),
			LayerInfo(display_name='Point sur mauvais plan', layer_name='105_verif_point_sur_mauvais_plan'),
			LayerInfo(display_name='Répartition des plans du lot', layer_name='105_itf_rp'),
			LayerInfo(
				display_name='Objet ponctuel hors du périmètre du lot',
				layer_name='112_itf_objet_hors_perimetrelot_point',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='nomtable',
				symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(3)},
				opacity=.5,
				visibility=False
			),
			LayerInfo(
				display_name='Objet linéaire hors du périmètre du lot',
				layer_name='112_itf_objet_hors_perimetrelot_ligne',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED,
				category_field='nomtable',
				symbology_data_defined_properties={QgsSymbolLayer.PropertyWidth: QgsProperty.fromValue(2)},
				opacity=.5,
				visibility=False
			),
			LayerInfo(
				display_name='Objet surfacique hors du périmètre du lot',
				layer_name='112_itf_objet_hors_perimetre_surface',
				symbology_type=SymbologyType.RANDOM_CATEGORIZED, 
				category_field='nomtable',
				symbology_data_defined_properties={QgsSymbolLayer.PropertyStrokeWidth: QgsProperty.fromValue(2)},
				opacity=.5,
				visibility=False
			),
			LayerInfo(display_name='Plans en vigueur à proximité du lot', layer_name='111_bdmo_repartition_plans_alentours'),
			LayerInfo(display_name='Périmetre du lot', layer_name='112_itf_mise_a_jourrp'), 
		)
		self.check_layer = (
			'point divergent entre les immeubles et la répartition des plans',
			'Sifflet entre les immeubles et la répartition des plans',
			"Point sur mauvais plan",u"Objet ponctuel hors du périmètre du lot",
			"Objet linéaire hors du périmètre du lot",u"Objet surfacique hors du périmètre du lot"
		)


class VerifContinuite_des_reseaux(SpatialiteData):
	"""Class used to load test on PF's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)
		self.group_name = u"Vérification des réseaux"
		# set layer's parameter in a dict list
		self.layer_infos = 	(	
			LayerInfo(
				display_name='CS Nom et numéro', 
				layer_name='002_ITF_CS_Pos_Surface_CS', 
				sql_request='"type" = "Nom_objet" AND ("number_name" LIKE "Route%" OR "number_name" LIKE "Ruisseau%" OR "number_name" LIKE "La%" OR "number_name" LIKE "Le%")'
			),
			LayerInfo(
				display_name='OD Nom et numéro', 
				layer_name='003_ITF_OD_Pos_Element_lineaire', 
				sql_request='"number_name" LIKE "Ligne%"'
			),
			LayerInfo(display_name='Cours d\'eau (DGE)', layer_name='112_DWH_Gesreau', opacity=.5),
			LayerInfo(display_name='Traversé de localité (DGMR)', layer_name='112_DWH_TraverseLocalite'),
			LayerInfo(display_name='Axes de maintenance du réseau routier (DGMR)', layer_name='112_dwh_axe'),
			LayerInfo(
				display_name='Couverture du sol',
				layer_name='002_ITF_CS_Surface_CS',
				sql_request='"vd_genre" IN ("eau.cours_eau", "revetement_dur.route_chemin","revetement_dur.chemin_de_fer")',
				opacity=.5
			),
			LayerInfo(
				display_name='Réseaux dans les objet divers linéaires',
				layer_name='003_ITF_OD_Element_lineaire',
				sql_request='"vd_genre" IN ("eau_canalisee_souterraine","tunnel_passage_inferieur_galerie","pont_passerelle","quai","ru","sentier","ligne_aerienne_a_haute_tension","mat_antenne","conduite_forcee","voie_ferree,telepherique","telecabine_telesiege","telepherique_de_chantier","skilift","bac","axe")'
			),
			LayerInfo(
				display_name='Réseaux dans les objet divers surfaciques',
				layer_name='003_ITF_OD_Element_surfacique',
				sql_request='"vd_genre" IN ("eau_canalisee_souterraine","tunnel_passage_inferieur_galerie","pont_passerelle","quai","ru","sentier","ligne_aerienne_a_haute_tension","mat_antenne","conduite_forcee","voie_ferree,telepherique","telecabine_telesiege","telepherique_de_chantier","skilift","bac","axe")'
			),
			LayerInfo(
				display_name='DP',
				layer_name='006_ITF_BF_Bien_fonds',
				sql_request='"number" LIKE "DP%"'),
			LayerInfo(display_name='Périmetre du lot', layer_name='112_itf_mise_a_jourrp'),
		)
		self.check_layer = (
			'CS Nom et numéro',
			"OD Nom et numéro",
			"Cours d'eau (DGE)",
			'Traversé de localité (DGMR)',
			'Couverture du sol',
			'Réseaux dans les objet divers linéaires',
			'Réseaux dans les objet divers surfaciques',
			'DP'
		)

class VerifPoints_fixes(SpatialiteData):
	"""Class used to load test on PF's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)
		self.group_name = u"Vérification des points fixes"
		# set layer's parameter in a dict list
		self.layer_infos = (	
			LayerInfo(
				display_name='Point fixes dont les attributs ITF vs BDMO ne sont pas identiques',
				layer_name='115_itf_pfp_problemeattribut',
				opacity=.5,
				visibility=False
			),
			LayerInfo(display_name='Points fixes en BDMO mais pas dans le fichier ITF', layer_name='115_bdmo_pfp_en_plus'),
			LayerInfo(display_name='Points fixes dans le fichier ITF mais pas en BDMO', layer_name='115_itf_pfp_en_plus', visibility=False),
			LayerInfo(display_name='PFP-PFA3', layer_name='001_itf_pf_points_fixes'),
			LayerInfo(display_name='Précision planimétrique des points fixes', layer_name='115_itf_pfp'),
			LayerInfo(display_name='Périmetre du lot', layer_name='112_itf_mise_a_jourrp'),
		)
		self.check_layer = (
			'Point fixes dont les attributs ITF vs BDMO ne sont pas identiques',
			'Points fixes en BDMO mais pas dans le fichier ITF',
			'Points fixes dans le fichier ITF mais pas en BDMO',
			'115_itf_pfp_en_plus'
		)


class VerifLimites_territoriales_et_administratives(SpatialiteData):
	"""Class used to load test on COM's layers"""
	def __init__(self, iface, pathSQliteDB):
		SpatialiteData.__init__(self, iface, pathSQliteDB)
		self.group_name = "Vérification des limites térritoriales et administratives"
		self.layer_infos = (	
			LayerInfo(
				display_name='Géometrie de limite de canton incorrecte (OGC)',
				layer_name='116_LigneCANT_OGC_fail',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 255, 0',
					'size': '2'
				}
			),
			LayerInfo(
				display_name='Géometrie de limite de commune incorrecte (OGC)',
				layer_name='116_LigneCOM_OGC_fail',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 255, 0',
					'size': '2'
				}
			),
			LayerInfo(
				display_name='Géometrie de limite de district incorrecte (OGC)',
				layer_name='116_LigneDIST_OGC_fail',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 255, 0',
					'size': '2'
				}
			),
			LayerInfo(
				display_name='point de limtes térritoriales manquant sous sommet de limite de commune',
				layer_name='116_PL_terr_manquant_sous_sommet_COM',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 255, 0',
					'size': '2'
				}),
			LayerInfo(
				display_name='sommet de limte de commune manquant sous point de limtes térritoriales',
				layer_name='116_Sommet_COM_manquant_sous_PL_terr',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 255, 0',
					'size': '2'
				}
			),
			LayerInfo(
				display_name='sommet de limte de commune manquant sous sommet de limite de canton',
				layer_name='116_sommetCOM_manquant_sous_sommet_CANT',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 255, 0',
					'size': '2'
				}
			),
			LayerInfo(
				display_name='sommet de limte decommune manquant sous sommet de limite de district',
				layer_name='116_sommetCOM_manquant_sous_sommet_Dist',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 255, 0',
					'size': '2'
				}
			),
			LayerInfo(
				display_name='point divergent entre les immeubles et la limite de commune',
				layer_name='103_VERIF_BF_COM_Point',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={
					'color': '255, 255, 0',
					'size': '2'
				}
			),
			LayerInfo(
				display_name='Sifflet entre les immeubles et la limite de commune',
				layer_name='103_VERIF_BF_COM_Surface',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={'color': '255, 0, 0'}
			),
			LayerInfo(display_name='Point limite térritoriale', layer_name='008_itf_lt_point_limite_ter'),
			LayerInfo(display_name='Limite commune', layer_name='008_itf_lt_limite_commune'),
			LayerInfo(display_name='Autre limite', layer_name='008_itf_lt_autre_limite'),
			LayerInfo(display_name='DDP', layer_name='006_ITF_BF_DDP', opacity=.5),
			LayerInfo(display_name='Biens fonds', layer_name='006_ITF_BF_Bien_fonds', opacity=.5)
		)
		self.check_layer = (
			'Géometrie de limite de canton incorrecte (OGC)',
			'Géometrie de limite de commune incorrecte (OGC)',
			'Géometrie de limite de district incorrecte (OGC)',
			'point de limtes térritoriales manquant sous sommet de limite de commune',
			'sommet de limte de commune manquant sous point de limtes térritoriales',
			'sommet de limte de commune manquant sous sommet de limite de canton',
			'sommet de limte decommune manquant sous sommet de limite de district',
			'point divergent entre les immeubles et la limite de commune',
			'Sifflet entre les immeubles et la limite de commune'
		)
