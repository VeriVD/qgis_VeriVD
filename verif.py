#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Connection class import
from spatialite import SpatialiteData

class VerifBiens_fonds(SpatialiteData):
	"""Class used to load test on BF's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Vérification - biens fonds"
		#set layer's parameter in a dict list
		self.infoLayer = 	(	
							[u"Sommet manquant sous un point limite",'100_verif_bf_sommet_manquant_sous_pl','',['qml'],'',''],
							[u"Sommet proche d'une limite","100_verif_bf_sommet_proche_pl",'',['qml'],'',''],
							[u"Point limite manquant sur un sommet",'100_verif_bf_pl_manquant_sur_sommet','',['qml'],'',''],
							[u'Point limite isolée','100_verif_bf_pl_isole','',['qml'],'',''],
							[u'Point limite avant point','100_verif_bf_pl_avant_point','',['qml'],'',''],
							[u'Point limite hors périmètre','100_verif_bf_pl_hors_perimetre','',['qml'],'',''],
							[u'Point limite en bordure du périmètre','100_verif_bf_pl_sur_bord_perimetre','',['qml'],'',''],
							[u"Point limite décrivant une limite quasi-alignée",'101_verif_bf_pl_aligne','',['qml'],'',''],
							[u"Ecart d'alignement",'101_verif_bf_distance_alignement','',['qml'],'',''],
							[u'Segment de biens fonds simplifié','101_verif_bf_segment_bf_modifie','',['qml'],'',''],
							[u'Segment de DDP simplifié','101_verif_ddp_segment_bf_modifie','',['qml'],'',''],
							[u'Précision planimétrique des points limites','100_verif_bf_pl_precplannum','',['qml'],'',''],
							[u'Point limite','006_ITF_BF_Point_limite','',['qml'],'',''],
							[u'Numéros des biens fonds','006_ITF_BF_Pos_Bien_fonds','',['qml'],'',''],
							[u'Numéros des DDP','006_ITF_BF_Pos_DDP','',['qml'],'',''],
							[u"DDP",'006_ITF_BF_DDP','',['qml'],'',''],
							[u'Biens fonds','006_ITF_BF_Bien_fonds','',['qml'],'',''],
							[u"Biens fonds à proximité du lot",'111_bdmo_biens_fonds_alentours','',['qml'],'',''],
							[u"Différence des surfaces des immeubles selon 6422bis",'107_verif_6422bis','',['qml'],'','no'],
							[u"Plans en vigueur à proximité du lot",'111_bdmo_repartition_plans_alentours','',['qml'],'',''],
							[u"Plans en vigueur du lot",'111_bdmo_repartition_plan_en_vigueur_du_lot','',['qml'],'','']
							)
		self.checkLayer = 	(u"Sommet manquant sous un point limite",u"Sommet proche d'une limite",u"Point limite manquant sur un sommet",u'Point limite isolée',u'Point limite avant point',u'Point limite en bordure du périmètre',u"Point limite décrivant une limite quasi-alignée")

class VerifNomenclature(SpatialiteData):
	"""Class used to load test on NO's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Vérification des sifflets sur les biens fonds"
		#set layer's parameter in a dict list
		self.infoLayer = 	(
							[u'point divergent entre les immeubles et la nomenclature','103_VERIF_BF_NO_Point','',['simple',{'color':'255,255,0','size':'4'}],'',''],
							[u'Sifflet entre les immeubles et la nomenclature','103_VERIF_BF_NO_Surface','',['simple',{'color':'255,0,0'}],'',''],
							[u'Nom local','005_ITF_NO_Nom_local','',['randomCategorized',{'field':'name'}],50,''],
							[u"DDP",'006_ITF_BF_DDP','',['qml'],'',''],
							[u'Biens fonds','006_ITF_BF_Bien_fonds','',['qml'],'','']
							)
		self.checkLayer = 	(u'point divergent entre les immeubles et la nomenclature',u'Sifflet entre les immeubles et la nomenclature')

class VerifAdresses(SpatialiteData):
	"""Class used to load test on BAT's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Vérification des adresses"
		#set layer's parameter in a dict list
		self.infoLayer = 	(	
							[u"Numéro d'entrée",'009_itf_bat_posentree_batiment','',['qml'],'',''],
							[u'Point de départ des tronçons','009_itf_bat_point_depart','',['qml'],'',''],
							[u'Entrée des bâtiments','009_itf_bat_entree_batiment','',['qml'],'',''],
							[u'Entrée du RCB','104_dwh_adresse_rcb','',['qml'],'','no'],
							[u'Différence entre les entrées de la MO et celles du RCB','104_verif_entreemo_diff_rcb','',['qml'],'','no'],
							[u'Raccord des entrées vers localisation','109_VERIF_Entree_Vers_Localisation','',['qml'],'',''],
							[u'Sens du tronçon','009_ITF_BAT_Troncon_rue','',['qml'],'',''],
							[u'Nom rue','009_ITF_BAT_Troncon_rue','',['randomCategorized',{'field':'texte','width':'3','capstyle':'round','joinstyle':'round'}],'',''], 
							[u'Habitation sans adresses','108_VERIF_Habitation_sans_adresse','',['simple',{'color':'255,0,0,180','border_color':'255,255,0'}],'','no'],
							[u'Bâtiment et surface en dur','002_ITF_CS_Surface_CS','"type" = "batiment" OR "vd_genre" LIKE "revetement_dur%"',['qml'],'',''],
							[u'DP','006_ITF_BF_Bien_fonds','"number" LIKE "DP%"',['simple',{'color':'255,255,255','border_color':'0,0,0','width_border':'0.5'}],'',''],
							[u'Couverture du sol','002_ITF_CS_Surface_CS','',['qml'],50,'']
							)
		self.checkLayer = 	(u"Numéro d'entrée",u'Nom rue',u'Point de départ des tronçons',u'Entrée des bâtiments',u'Entrée du RCB',u'Différence entre les entrées de la MO et celles du RCB',u'Raccord des entrées vers localisation',u'Sens du tronçon')

class VerifCouverture_du_sol_et_objets_divers(SpatialiteData):
	"""Class used to load test on CS's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Vérification de la couverture du sol et des objets divers"
		#set layer's parameter in a dict list
		self.infoLayer = 	(	
							[u'OD - Element surfacique qui devrait être linéaire','114_VERIF_OD_surfaciqueErreur','',['simple',{'color':'255,0,0','width_border':'2'}],'',''],
							[u'OD - Element linéaire qui devrait être surfacique','114_VERIF_OD_lineaireErreur','',['simple',{'color':'255,0,0','width':'2'}],'',''],
							[u'Point particulier CS manquant sous un angle de bâtiment','113_cs_pointbatiment','',['simple',{'color':'255,100,200','size':'2'}],'',''],
							[u"Validation OGC des objets divers",'110_od_ogc_geometrie','',['randomCategorized',{'field':'issue_found','width':'2'}],'',''],
							[u'point divergent entre les immeubles et la couverture du sol','103_verif_bf_cs_point','',['simple',{'color':'255,255,0','size':'2'}],'',''],
							[u'Sifflet entre les immeubles et la couverture du sol','103_verif_bf_cs_surface','',['simple',{'color':'255,0,0'}],'',''],
							[u"Nombre de géomètrie par objet divers linéaires",'102_verif_od_lineaire_fid','',['qml'],'',''],
							[u"Nombre de géomètrie par objet divers surfacique",'102_verif_od_surfacique_fid','',['qml'],'',''],
							[u"Objets divers linéaires (relation vers les géomètries)",'102_verif_od_lineaire_fid','',['randomCategorized',{'field':'fid_od','width':'3'}],50,''],
							[u"Objets divers surfaciques (relation vers les géomètries)",'102_verif_od_surfacique_fid','',['randomCategorized',{'field':'fid_od','width':'3'}],50,''],
							[u'OD linéaire','003_ITF_OD_Element_lineaire','',['qml'],'',''],
							[u'OD surfacique','003_ITF_OD_Element_surfacique','',['qml'],'',''],
							[u"OD point particulier",'003_ITF_OD_Point_particulier','',['qml'],'',''],
							[u"OD Nom et Numéro ligne",'003_ITF_OD_Pos_Element_lineaire','',['qml'],'',''],
							[u"OD Nom et Numéro surface",'003_ITF_OD_Pos_Element_surfacique','',['qml'],'',''],
							[u'Nom et numéro CS','002_ITF_CS_Pos_Surface_CS','',['qml'],'',''],
							[u"Point particulier CS",'002_ITF_CS_Point_particulier','',['qml'],'',''],
							[u'Bâtiment','002_ITF_CS_Surface_CS','"type" = "batiment"',['simple',{'color':'255,210,210'}],'',''],
							[u"DDP",'006_ITF_BF_DDP','',['qml'],'',''],
							[u'Biens fonds','006_ITF_BF_Bien_fonds','',['qml'],'',''],
							[u'Surface CS','002_ITF_CS_Surface_CS','',['qml'],50,'']
							)
		self.checkLayer = 	(u'OD - Element surfacique qui devrait être linéaire',u'OD - Element linéaire qui devrait être surfacique',u'Point particulier CS manquant sous un angle de bâtiment',u"Validation OGC des objets divers",u'point divergent entre les immeubles et la couverture du sol',u'Sifflet entre les immeubles et la couverture du sol',u"Nombre de géomètrie par objet divers linéaires",u"Nombre de géomètrie par objet divers surfacique",u"Objets divers linéaires (relation vers les géomètries)",u"Objets divers surfaciques (relation vers les géomètries)")

class VerifRepartition_des_plans_et_domaine_de_numerotation(SpatialiteData):
	"""Class used to load test on RP's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Vérification de la répartition des plans et de la numérotation des points"
		#set layer's parameter in a dict list
		self.infoLayer = 	(	
							[u'point divergent entre les immeubles et la répartition des plans','103_VERIF_BF_RP_Point','',['simple',{'color':'255,255,0','size':'2'}],'',''],
							[u'Sifflet entre les immeubles et la répartition des plans','103_VERIF_BF_RP_Surface','',['simple',{'color':'255,0,0'}],'',''],
							[u"Point sur mauvais plan",'105_verif_point_sur_mauvais_plan','',['qml'],'',''],
							[u"Répartition des plans du lot",'105_itf_rp','',['qml'],'',''],
							[u"Objet ponctuel hors du périmètre du lot",'112_itf_objet_hors_perimetrelot_point','',['randomCategorized',{'field':'nomtable','size':'3'}],50,'no'],
							[u"Objet linéaire hors du périmètre du lot",'112_itf_objet_hors_perimetrelot_ligne','',['randomCategorized',{'field':'nomtable','width':'2'}],50,'no'],
							[u"Objet surfacique hors du périmètre du lot",'112_itf_objet_hors_perimetre_surface','',['randomCategorized',{'field':'nomtable','width_border':'2'}],50,'no'],
							[u"Plans en vigueur à proximité du lot",'111_bdmo_repartition_plans_alentours','',['qml'],'',''],
							[u"Périmetre du lot",'112_itf_mise_a_jourrp','',['qml'],'','']
							)
		self.checkLayer = 	(u'point divergent entre les immeubles et la répartition des plans',u'Sifflet entre les immeubles et la répartition des plans',u"Point sur mauvais plan",u"Objet ponctuel hors du périmètre du lot",u"Objet linéaire hors du périmètre du lot",u"Objet surfacique hors du périmètre du lot")

class VerifContinuite_des_reseaux(SpatialiteData):
	"""Class used to load test on PF's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Vérification des réseaux"
		#set layer's parameter in a dict list
		self.infoLayer = 	(	
							[u'CS Nom et numéro','002_ITF_CS_Pos_Surface_CS','"type" = "Nom_objet" AND ("number_name" LIKE "Route%" OR "number_name" LIKE "Ruisseau%" OR "number_name" LIKE "La%" OR "number_name" LIKE "Le%")',['qml'],'',''],
							[u"OD Nom et numéro",'003_ITF_OD_Pos_Element_lineaire','"number_name" LIKE "Ligne%"',['qml'],'',''],
							[u"Cours d'eau (DGE)",'112_DWH_Gesreau','',['qml'],50,''],
							[u'Traversé de localité (DGMR)','112_DWH_TraverseLocalite','',['qml'],'',''],
							[u'Axes de maintenance du réseau routier (DGMR)','112_dwh_axe','',['qml'],'',''],
							[u'Couverture du sol','002_ITF_CS_Surface_CS','"vd_genre" IN ("eau.cours_eau", "revetement_dur.route_chemin","revetement_dur.chemin_de_fer")',['qml'],50,''],
							[u'Réseaux dans les objet divers linéaires','003_ITF_OD_Element_lineaire','"vd_genre" IN ("eau_canalisee_souterraine","tunnel_passage_inferieur_galerie","pont_passerelle","quai","ru","sentier","ligne_aerienne_a_haute_tension","mat_antenne","conduite_forcee","voie_ferree,telepherique","telecabine_telesiege","telepherique_de_chantier","skilift","bac","axe")',['qml'],'',''],
							[u'Réseaux dans les objet divers surfaciques','003_ITF_OD_Element_surfacique','"vd_genre" IN ("eau_canalisee_souterraine","tunnel_passage_inferieur_galerie","pont_passerelle","quai","ru","sentier","ligne_aerienne_a_haute_tension","mat_antenne","conduite_forcee","voie_ferree,telepherique","telecabine_telesiege","telepherique_de_chantier","skilift","bac","axe")',['qml'],'',''],
							[u'DP','006_ITF_BF_Bien_fonds','"number" LIKE "DP%"',['qml'],'',''],
							[u"Périmetre du lot",'112_itf_mise_a_jourrp','',['qml'],'','']
							)
		self.checkLayer = 	(u'CS Nom et numéro',u"OD Nom et numéro",u"Cours d'eau (DGE)",u'Traversé de localité (DGMR)',u'Couverture du sol',u'Réseaux dans les objet divers linéaires',u'Réseaux dans les objet divers surfaciques',u'DP')

class VerifPoints_fixes(SpatialiteData):
	"""Class used to load test on PF's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Vérification des points fixes"
		#set layer's parameter in a dict list
		self.infoLayer = 	(	
							[u'Point fixes dont les attributs ITF vs BDMO ne sont pas identiques','115_itf_pfp_problemeattribut','',['qml'],50,'no'],
							[u'Points fixes en BDMO mais pas dans le fichier ITF','115_bdmo_pfp_en_plus','',['qml'],'',''],
							[u'Points fixes dans le fichier ITF mais pas en BDMO','115_itf_pfp_en_plus','',['qml'],'','no'],
							[u'PFP-PFA3','001_itf_pf_points_fixes','',['qml'],'',''],
							[u'Précision planimétrique des points fixes','115_itf_pfp','',['qml'],'',''],
							[u"Périmetre du lot",'112_itf_mise_a_jourrp','',['qml'],'','']
							)
		self.checkLayer = 	(u'Point fixes dont les attributs ITF vs BDMO ne sont pas identiques',u'Points fixes en BDMO mais pas dans le fichier ITF',u'Points fixes dans le fichier ITF mais pas en BDMO','115_itf_pfp_en_plus')

class VerifLimites_territoriales_et_administratives(SpatialiteData):
	"""Class used to load test on COM's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Vérification des limites térritoriales et administratives"
		self.infoLayer = 	(	
							[u'Géometrie de limite de canton incorrecte (OGC)','116_LigneCANT_OGC_fail','',['simple',{'color':'255,255,0','size':'2'}],'',''],
							[u'Géometrie de limite de commune incorrecte (OGC)','116_LigneCOM_OGC_fail','',['simple',{'color':'255,255,0','size':'2'}],'',''],
							[u'Géometrie de limite de district incorrecte (OGC)','116_LigneDIST_OGC_fail','',['simple',{'color':'255,255,0','size':'2'}],'',''],
							[u'point de limtes térritoriales manquant sous sommet de limite de commune','116_PL_terr_manquant_sous_sommet_COM','',['simple',{'color':'255,255,0','size':'2'}],'',''],
							[u'sommet de limte de commune manquant sous point de limtes térritoriales','116_Sommet_COM_manquant_sous_PL_terr','',['simple',{'color':'255,255,0','size':'2'}],'',''],
							[u'sommet de limte de commune manquant sous sommet de limite de canton','116_sommetCOM_manquant_sous_sommet_CANT','',['simple',{'color':'255,255,0','size':'2'}],'',''],
							[u'sommet de limte decommune manquant sous sommet de limite de district','116_sommetCOM_manquant_sous_sommet_Dist','',['simple',{'color':'255,255,0','size':'2'}],'',''],
							[u'point divergent entre les immeubles et la limite de commune','103_VERIF_BF_COM_Point','',['simple',{'color':'255,255,0','size':'2'}],'',''],
							[u'Sifflet entre les immeubles et la limite de commune','103_VERIF_BF_COM_Surface','',['simple',{'color':'255,0,0'}],'',''],
							[u"Point limite térritoriale",'008_itf_lt_point_limite_ter','',['qml'],'',''],
							[u'Limite commune','008_itf_lt_limite_commune','',['qml'],'',''],
							[u'Autre limite','008_itf_lt_autre_limite','',['qml'],'',''],
							[u"DDP",'006_ITF_BF_DDP','',['qml'],50,''],
							[u'Biens fonds','006_ITF_BF_Bien_fonds','',['qml'],50,'']
							)
		self.checkLayer = 	(u'Géometrie de limite de canton incorrecte (OGC)',u'Géometrie de limite de commune incorrecte (OGC)',u'Géometrie de limite de district incorrecte (OGC)',u'point de limtes térritoriales manquant sous sommet de limite de commune',u'sommet de limte de commune manquant sous point de limtes térritoriales',u'sommet de limte de commune manquant sous sommet de limite de canton',u'sommet de limte decommune manquant sous sommet de limite de district',u'point divergent entre les immeubles et la limite de commune',u'Sifflet entre les immeubles et la limite de commune')