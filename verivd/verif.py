#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .spatialite import SpatialiteData


class VerifBiens_fonds(SpatialiteData):
	"""Class used to load test on BF's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.group_name = u"Vérification - biens fonds"
		# set layer's parameter in a dict list
		self.infoLayer = (	
			["Sommet manquant sous un point limite", '100_verif_bf_sommet_manquant_sous_pl', '', ['qml'], '', ''],
			["Sommet proche d'une limite", "100_verif_bf_sommet_proche_pl", '', ['qml'], '', ''],
			["Point limite manquant sur un sommet",'100_verif_bf_pl_manquant_sur_sommet', '', ['qml'], '', ''],
			['Point limite isolée', '100_verif_bf_pl_isole', '', ['qml'], '', ''],
			['Point limite avant point', '100_verif_bf_pl_avant_point', '', ['qml'], '', ''],
			['Point limite hors périmètre', '100_verif_bf_pl_hors_perimetre', '', ['qml'], '', ''],
			['Point limite en bordure du périmètre', '100_verif_bf_pl_sur_bord_perimetre', '', ['qml'], '', ''],
			["Point limite décrivant une limite quasi-alignée",'101_verif_bf_pl_aligne', '', ['qml'], '', ''],
			["Ecart d'alignement",'101_verif_bf_distance_alignement', '', ['qml'], '', ''],
			['Segment de biens fonds simplifié', '101_verif_bf_segment_bf_modifie', '', ['qml'], '', ''],
			['Segment de DDP simplifié', '101_verif_ddp_segment_bf_modifie', '', ['qml'], '', ''],
			['Précision planimétrique des points limites', '100_verif_bf_pl_precplannum', '', ['qml'], '', ''],
			['Point limite', '006_ITF_BF_Point_limite', '', ['qml'], '', ''],
			['Numéros des biens fonds', '006_ITF_BF_Pos_Bien_fonds', '', ['qml'], '', ''],
			['Numéros des DDP', '006_ITF_BF_Pos_DDP', '', ['qml'], '', ''],
			["DDP",'006_ITF_BF_DDP', '', ['qml'], '', ''],
			['Biens fonds', '006_ITF_BF_Bien_fonds', '', ['qml'], '', ''],
			["Biens fonds à proximité du lot",'111_bdmo_biens_fonds_alentours', '', ['qml'], '', ''],
			["Différence des surfaces des immeubles selon 6422bis",'107_verif_6422bis', '', ['qml'], '', 'no'],
			["Plans en vigueur à proximité du lot",'111_bdmo_repartition_plans_alentours', '', ['qml'], '', ''],
			["Plans en vigueur du lot",'111_bdmo_repartition_plan_en_vigueur_du_lot', '', ['qml'], '', '']
		)
		self.check_layer = (
			"Sommet manquant sous un point limite",
			"Sommet proche d'une limite",
			"Point limite manquant sur un sommet",
			'Point limite isolée',
			'Point limite avant point',
			'Point limite en bordure du périmètre',
			"Point limite décrivant une limite quasi-alignée"
		)

class VerifNomenclature(SpatialiteData):
	"""Class used to load test on NO's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.group_name = u"Vérification des sifflets sur les biens fonds"
		# set layer's parameter in a dict list
		self.infoLayer = (
			['point divergent entre les immeubles et la nomenclature', '103_VERIF_BF_NO_Point', '', ['simple', {'color': '255,255,0', 'size':'4'}], '', ''],
			['Sifflet entre les immeubles et la nomenclature', '103_VERIF_BF_NO_Surface', '', ['simple', {'color': '255,0,0'}], '', ''],
			['Nom local', '005_ITF_NO_Nom_local', '', ['randomCategorized', {'field':'name'}], 50, ''],
			["DDP",'006_ITF_BF_DDP', '', ['qml'], '', ''],
			['Biens fonds', '006_ITF_BF_Bien_fonds', '', ['qml'], '', '']
		)
		self.check_layer = (
			'point divergent entre les immeubles et la nomenclature',
			'Sifflet entre les immeubles et la nomenclature'
		)

class VerifAdresses(SpatialiteData):
	"""Class used to load test on BAT's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.group_name = u"Vérification des adresses"
		# set layer's parameter in a dict list
		self.infoLayer = 	(	
			["Numéro d'entrée",'009_itf_bat_posentree_batiment', '', ['qml'], '', ''],
			['Point de départ des tronçons', '009_itf_bat_point_depart', '', ['qml'], '', ''],
			['Entrée des bâtiments', '009_itf_bat_entree_batiment', '', ['qml'], '', ''],
			['Entrée du RCB', '104_dwh_adresse_rcb', '', ['qml'], '', 'no'],
			['Différence entre les entrées de la MO et celles du RCB', '104_verif_entreemo_diff_rcb', '', ['qml'], '', 'no'],
			['Raccord des entrées vers localisation', '109_VERIF_Entree_Vers_Localisation', '', ['qml'], '', ''],
			['Sens du tronçon', '009_ITF_BAT_Troncon_rue', '', ['qml'], '', ''],
			['Nom rue', '009_ITF_BAT_Troncon_rue', '', ['randomCategorized', {'field':'texte', 'width':'3', 'capstyle':'round', 'joinstyle':'round'}], '', ''], 
			['Habitation sans adresses', '108_VERIF_Habitation_sans_adresse', '', ['simple', {'color': '255,0,0,180', 'border_color':'255,255,0'}], '', 'no'],
			['Bâtiment et surface en dur', '002_ITF_CS_Surface_CS', '"type" = "batiment" OR "vd_genre" LIKE "revetement_dur%"', ['qml'], '', ''],
			['DP', '006_ITF_BF_Bien_fonds', '"number" LIKE "DP%"', ['simple', {'color': '255,255,255', 'border_color':'0,0,0', 'width_border':'0.5'}], '', ''],
			['Couverture du sol', '002_ITF_CS_Surface_CS', '', ['qml'], 50, '']
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
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.group_name = u"Vérification de la couverture du sol et des objets divers"
		# set layer's parameter in a dict list
		self.infoLayer = 	(	
			['OD - Element surfacique qui devrait être linéaire', '114_VERIF_OD_surfaciqueErreur', '', ['simple', {'color': '255,0,0', 'width_border':'2'}], '', ''],
			['OD - Element linéaire qui devrait être surfacique', '114_VERIF_OD_lineaireErreur', '', ['simple', {'color': '255,0,0', 'width':'2'}], '', ''],
			['Point particulier CS manquant sous un angle de bâtiment', '113_cs_pointbatiment', '', ['simple', {'color': '255,100,200', 'size':'2'}], '', ''],
			["Validation OGC des objets divers",'110_od_ogc_geometrie', '', ['randomCategorized', {'field':'issue_found', 'width':'2'}], '', ''],
			['point divergent entre les immeubles et la couverture du sol', '103_verif_bf_cs_point', '', ['simple', {'color': '255,255,0', 'size':'2'}], '', ''],
			['Sifflet entre les immeubles et la couverture du sol', '103_verif_bf_cs_surface', '', ['simple', {'color': '255,0,0'}], '', ''],
			["Nombre de géomètrie par objet divers linéaires",'102_verif_od_lineaire_fid', '', ['qml'], '', ''],
			["Nombre de géomètrie par objet divers surfacique",'102_verif_od_surfacique_fid', '', ['qml'], '', ''],
			["Objets divers linéaires (relation vers les géomètries)",'102_verif_od_lineaire_fid', '', ['randomCategorized', {'field':'fid_od', 'width':'3'}], 50, ''],
			["Objets divers surfaciques (relation vers les géomètries)",'102_verif_od_surfacique_fid', '', ['randomCategorized', {'field':'fid_od', 'width':'3'}], 50, ''],
			['OD linéaire', '003_ITF_OD_Element_lineaire', '', ['qml'], '', ''],
			['OD surfacique', '003_ITF_OD_Element_surfacique', '', ['qml'], '', ''],
			["OD point particulier",'003_ITF_OD_Point_particulier', '', ['qml'], '', ''],
			["OD Nom et Numéro ligne",'003_ITF_OD_Pos_Element_lineaire', '', ['qml'], '', ''],
			["OD Nom et Numéro surface",'003_ITF_OD_Pos_Element_surfacique', '', ['qml'], '', ''],
			['Nom et numéro CS', '002_ITF_CS_Pos_Surface_CS', '', ['qml'], '', ''],
			["Point particulier CS",'002_ITF_CS_Point_particulier', '', ['qml'], '', ''],
			['Bâtiment', '002_ITF_CS_Surface_CS', '"type" = "batiment"', ['simple', {'color': '255,210,210'}], '', ''],
			["DDP",'006_ITF_BF_DDP', '', ['qml'], '', ''],
			['Biens fonds', '006_ITF_BF_Bien_fonds', '', ['qml'], '', ''],
			['Surface CS', '002_ITF_CS_Surface_CS', '', ['qml'], 50, '']
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
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.group_name = u"Vérification de la répartition des plans et de la numérotation des points"
		# set layer's parameter in a dict list
		self.infoLayer = (	
			['point divergent entre les immeubles et la répartition des plans', '103_VERIF_BF_RP_Point', '', ['simple', {'color': '255,255,0', 'size':'2'}], '', ''],
			['Sifflet entre les immeubles et la répartition des plans', '103_VERIF_BF_RP_Surface', '', ['simple', {'color': '255,0,0'}], '', ''],
			["Point sur mauvais plan",'105_verif_point_sur_mauvais_plan', '', ['qml'], '', ''],
			["Répartition des plans du lot",'105_itf_rp', '', ['qml'], '', ''],
			["Objet ponctuel hors du périmètre du lot",'112_itf_objet_hors_perimetrelot_point', '', ['randomCategorized', {'field':'nomtable', 'size':'3'}], 50,'no'],
			["Objet linéaire hors du périmètre du lot",'112_itf_objet_hors_perimetrelot_ligne', '', ['randomCategorized', {'field':'nomtable', 'width':'2'}], 50,'no'],
			["Objet surfacique hors du périmètre du lot",'112_itf_objet_hors_perimetre_surface', '', ['randomCategorized', {'field':'nomtable', 'width_border':'2'}], 50,'no'],
			["Plans en vigueur à proximité du lot",'111_bdmo_repartition_plans_alentours', '', ['qml'], '', ''],
			["Périmetre du lot",'112_itf_mise_a_jourrp', '', ['qml'], '', '']
		)
		self.check_layer = (
			'point divergent entre les immeubles et la répartition des plans',
			'Sifflet entre les immeubles et la répartition des plans',
			"Point sur mauvais plan",u"Objet ponctuel hors du périmètre du lot",
			"Objet linéaire hors du périmètre du lot",u"Objet surfacique hors du périmètre du lot"
		)

class VerifContinuite_des_reseaux(SpatialiteData):
	"""Class used to load test on PF's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.group_name = u"Vérification des réseaux"
		# set layer's parameter in a dict list
		self.infoLayer = 	(	
			['CS Nom et numéro', '002_ITF_CS_Pos_Surface_CS', '"type" = "Nom_objet" AND ("number_name" LIKE "Route%" OR "number_name" LIKE "Ruisseau%" OR "number_name" LIKE "La%" OR "number_name" LIKE "Le%")', ['qml'], '', ''],
			["OD Nom et numéro",'003_ITF_OD_Pos_Element_lineaire', '"number_name" LIKE "Ligne%"', ['qml'], '', ''],
			["Cours d'eau (DGE)",'112_DWH_Gesreau', '', ['qml'], 50, ''],
			['Traversé de localité (DGMR)', '112_DWH_TraverseLocalite', '', ['qml'], '', ''],
			['Axes de maintenance du réseau routier (DGMR)', '112_dwh_axe', '', ['qml'], '', ''],
			['Couverture du sol', '002_ITF_CS_Surface_CS', '"vd_genre" IN ("eau.cours_eau", "revetement_dur.route_chemin","revetement_dur.chemin_de_fer")', ['qml'], 50, ''],
			['Réseaux dans les objet divers linéaires', '003_ITF_OD_Element_lineaire', '"vd_genre" IN ("eau_canalisee_souterraine","tunnel_passage_inferieur_galerie","pont_passerelle","quai","ru","sentier","ligne_aerienne_a_haute_tension","mat_antenne","conduite_forcee","voie_ferree,telepherique","telecabine_telesiege","telepherique_de_chantier","skilift","bac","axe")', ['qml'], '', ''],
			['Réseaux dans les objet divers surfaciques', '003_ITF_OD_Element_surfacique', '"vd_genre" IN ("eau_canalisee_souterraine","tunnel_passage_inferieur_galerie","pont_passerelle","quai","ru","sentier","ligne_aerienne_a_haute_tension","mat_antenne","conduite_forcee","voie_ferree,telepherique","telecabine_telesiege","telepherique_de_chantier","skilift","bac","axe")', ['qml'], '', ''],
			['DP', '006_ITF_BF_Bien_fonds', '"number" LIKE "DP%"', ['qml'], '', ''],
			["Périmetre du lot",'112_itf_mise_a_jourrp', '', ['qml'], '', '']
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
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.group_name = u"Vérification des points fixes"
		# set layer's parameter in a dict list
		self.infoLayer = (	
			['Point fixes dont les attributs ITF vs BDMO ne sont pas identiques', '115_itf_pfp_problemeattribut', '', ['qml'], 50,'no'],
			['Points fixes en BDMO mais pas dans le fichier ITF', '115_bdmo_pfp_en_plus', '', ['qml'], '', ''],
			['Points fixes dans le fichier ITF mais pas en BDMO', '115_itf_pfp_en_plus', '', ['qml'], '', 'no'],
			['PFP-PFA3', '001_itf_pf_points_fixes', '', ['qml'], '', ''],
			['Précision planimétrique des points fixes', '115_itf_pfp', '', ['qml'], '', ''],
			["Périmetre du lot",'112_itf_mise_a_jourrp', '', ['qml'], '', '']
		)
		self.check_layer = (
			'Point fixes dont les attributs ITF vs BDMO ne sont pas identiques',
			'Points fixes en BDMO mais pas dans le fichier ITF',
			'Points fixes dans le fichier ITF mais pas en BDMO',
			'115_itf_pfp_en_plus'
		)

class VerifLimites_territoriales_et_administratives(SpatialiteData):
	"""Class used to load test on COM's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.group_name = "Vérification des limites térritoriales et administratives"
		self.infoLayer = (	
			['Géometrie de limite de canton incorrecte (OGC)', '116_LigneCANT_OGC_fail', '', ['simple', {'color': '255,255,0', 'size':'2'}], '', ''],
			['Géometrie de limite de commune incorrecte (OGC)', '116_LigneCOM_OGC_fail', '', ['simple', {'color': '255,255,0', 'size':'2'}], '', ''],
			['Géometrie de limite de district incorrecte (OGC)', '116_LigneDIST_OGC_fail', '', ['simple', {'color': '255,255,0', 'size':'2'}], '', ''],
			['point de limtes térritoriales manquant sous sommet de limite de commune', '116_PL_terr_manquant_sous_sommet_COM', '', ['simple', {'color': '255,255,0', 'size':'2'}], '', ''],
			['sommet de limte de commune manquant sous point de limtes térritoriales', '116_Sommet_COM_manquant_sous_PL_terr', '', ['simple', {'color': '255,255,0', 'size':'2'}], '', ''],
			['sommet de limte de commune manquant sous sommet de limite de canton', '116_sommetCOM_manquant_sous_sommet_CANT', '', ['simple', {'color': '255,255,0', 'size':'2'}], '', ''],
			['sommet de limte decommune manquant sous sommet de limite de district', '116_sommetCOM_manquant_sous_sommet_Dist', '', ['simple', {'color': '255,255,0', 'size':'2'}], '', ''],
			['point divergent entre les immeubles et la limite de commune', '103_VERIF_BF_COM_Point', '', ['simple', {'color': '255,255,0', 'size':'2'}], '', ''],
			['Sifflet entre les immeubles et la limite de commune', '103_VERIF_BF_COM_Surface', '', ['simple', {'color': '255,0,0'}], '', ''],
			["Point limite térritoriale",'008_itf_lt_point_limite_ter', '', ['qml'], '', ''],
			['Limite commune', '008_itf_lt_limite_commune', '', ['qml'], '', ''],
			['Autre limite', '008_itf_lt_autre_limite', '', ['qml'], '', ''],
			["DDP",'006_ITF_BF_DDP', '', ['qml'], 50, ''],
			['Biens fonds', '006_ITF_BF_Bien_fonds', '', ['qml'], 50, '']
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