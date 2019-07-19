#!/usr/bin/env python
# -*- coding: utf-8 -*-


from qgis.core import QgsSymbolLayer
from qgis.PyQt.QtGui import QColor
from verivd.spatialite import SpatialiteData, LayerInfo, SymbologyType


# display_name, layerName, sqlRequest, symb, trans, visib

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
			LayerInfo(display_name='Point limite isolée', layer_name='100_verif_bf_pl_isole'),
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
			LayerInfo(display_name='Différence des surfaces des immeubles selon 6422bis', layer_name='107_verif_6422bis', visible=False),
			LayerInfo(display_name='Plans en vigueur à proximité du lot', layer_name='111_bdmo_repartition_plans_alentours'),
			LayerInfo(display_name='Plans en vigueur du lot', layer_name='111_bdmo_repartition_plan_en_vigueur_du_lot')
		)
		self.check_layer = (
			'Sommet manquant sous un point limite',
			'Sommet proche d\'une limite',
			'Point limite manquant sur un sommet',
			'Point limite isolée',
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
					QgsSymbolLayer.PropertyFillColor: QVariant.fromValue(QColor(255, 255, 0)),
					QgsSymbolLayer.PropertySize: QVariant.fromValue(4)
				}
			),
			LayerInfo(
				display_name='Sifflet entre les immeubles et la nomenclature',
				layer_name='103_VERIF_BF_NO_Surface',
				symbology_type=SymbologyType.SIMPLE,
				symbology_properties={QgsSymbolLayer.PropertyFillColor: QVariant.fromValue(QColor(255, 0, 0))}
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
			LayerInfo(display_name='Entrée du RCB', layer_name='104_dwh_adresse_rcb', visible=False),
			LayerInfo(display_name='Différence entre les entrées de la MO et celles du RCB', layer_name='104_verif_entreemo_diff_rcb', visible=False),
			LayerInfo(display_name='Raccord des entrées vers localisation', layer_name='109_VERIF_Entree_Vers_Localisation'),
			LayerInfo(display_name='Sens du tronçon', layer_name='009_ITF_BAT_Troncon_rue'),
			LayerInfo(
				display_name='Nom rue',
				layer_name='009_ITF_BAT_Troncon_rue',
				symbology_type=RANDOM_CATEGORIZED,

				['randomCategorized', {'field':'texte', 'width':'3', 'capstyle':'round', layer_name='joinstyle':'round'}], ''''],
			LayerInfo(display_name='Habitation sans adresses', layer_name='108_VERIF_Habitation_sans_adresse', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,0,0,180', QgsSymbolLayer.PropertyStrokeColor: '255,255,0'}], '''no'],
			LayerInfo(display_name='Bâtiment et surface en dur', layer_name='002_ITF_CS_Surface_CS', layer_name='"type" = "batiment" OR "vd_genre" LIKE "revetement_dur%"', ['qml'], ''''],
			LayerInfo(display_name='DP', '006_ITF_BF_Bien_fonds', layer_name='"number" LIKE "DP%"', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,255', QgsSymbolLayer.PropertyStrokeColor: '0,0,0', layer_name='width_border':'0.5'}], ''''],
			LayerInfo(display_name='Couverture du sol', layer_name='002_ITF_CS_Surface_CS', layer_name=''['qml'], 50, '']
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
			LayerInfo(display_name='OD - Element surfacique qui devrait être linéaire', '114_VERIF_OD_surfaciqueErreur', '', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,0,0', layer_name='width_border':'2'}], ''''],
			LayerInfo(display_name='OD - Element linéaire qui devrait être surfacique', '114_VERIF_OD_lineaireErreur', '', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,0,0', layer_name='width':'2'}], ''''],
			LayerInfo(display_name='Point particulier CS manquant sous un angle de bâtiment', '113_cs_pointbatiment', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,100,200', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='Validation OGC des objets divers",'110_od_ogc_geometrie', '', ['randomCategorized', {'field':'issue_found', layer_name='width':'2'}], ''''],
			LayerInfo(display_name='point divergent entre les immeubles et la couverture du sol', '103_verif_bf_cs_point', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,0', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='Sifflet entre les immeubles et la couverture du sol', '103_verif_bf_cs_surface', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,0,0'}], ''''],
			LayerInfo(display_name='Nombre de géomètrie par objet divers linéaires",'102_verif_od_lineaire_fid', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='Nombre de géomètrie par objet divers surfacique",'102_verif_od_surfacique_fid', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='Objets divers linéaires (relation vers les géomètries)",'102_verif_od_lineaire_fid', layer_name='', ['randomCategorized', {'field':'fid_od''width':'3'}], 50, ''],
			LayerInfo(display_name='Objets divers surfaciques (relation vers les géomètries)",'102_verif_od_surfacique_fid', layer_name='', ['randomCategorized', {'field':'fid_od''width':'3'}], 50, ''],
			LayerInfo(display_name='OD linéaire', layer_name='003_ITF_OD_Element_lineaire'),
			LayerInfo(display_name='OD surfacique', layer_name='003_ITF_OD_Element_surfacique'),
			LayerInfo(display_name='OD point particulier",'003_ITF_OD_Point_particulier', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='OD Nom et Numéro ligne",'003_ITF_OD_Pos_Element_lineaire', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='OD Nom et Numéro surface",'003_ITF_OD_Pos_Element_surfacique', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='Nom et numéro CS', layer_name='002_ITF_CS_Pos_Surface_CS'),
			LayerInfo(display_name='Point particulier CS",'002_ITF_CS_Point_particulier', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='Bâtiment', '002_ITF_CS_Surface_CS', layer_name='"type" = "batiment"', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,210,210'}], ''''],
			LayerInfo(display_name='DDP",'006_ITF_BF_DDP', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='Biens fonds', layer_name='006_ITF_BF_Bien_fonds'),
			LayerInfo(display_name='Surface CS', '002_ITF_CS_Surface_CS', layer_name=''['qml'], 50, '']
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
			LayerInfo(display_name='point divergent entre les immeubles et la répartition des plans', '103_VERIF_BF_RP_Point', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,0', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='Sifflet entre les immeubles et la répartition des plans', '103_VERIF_BF_RP_Surface', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,0,0'}], ''''],
			LayerInfo(display_name='Point sur mauvais plan",'105_verif_point_sur_mauvais_plan', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='Répartition des plans du lot",'105_itf_rp', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='Objet ponctuel hors du périmètre du lot",'112_itf_objet_hors_perimetrelot_point', layer_name='', ['randomCategorized', {'field':'nomtable'QgsSymbolLayer.PropertySize:'3'}], 50,'no'],
			LayerInfo(display_name='Objet linéaire hors du périmètre du lot",'112_itf_objet_hors_perimetrelot_ligne', layer_name='', ['randomCategorized', {'field':'nomtable''width':'2'}], 50,'no'],
			LayerInfo(display_name='Objet surfacique hors du périmètre du lot",'112_itf_objet_hors_perimetre_surface', layer_name='', ['randomCategorized', {'field':'nomtable''width_border':'2'}], 50,'no'],
			LayerInfo(display_name='Plans en vigueur à proximité du lot",'111_bdmo_repartition_plans_alentours', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='Périmetre du lot",'112_itf_mise_a_jourrp', layer_name='', ['qml'], '''']
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
			LayerInfo(display_name='CS Nom et numéro', '002_ITF_CS_Pos_Surface_CS', layer_name='"type" = "Nom_objet" AND ("number_name" LIKE "Route%" OR "number_name" LIKE "Ruisseau%" OR "number_name" LIKE "La%" OR "number_name" LIKE "Le%")', ['qml'], ''''],
			LayerInfo(display_name='OD Nom et numéro",'003_ITF_OD_Pos_Element_lineaire', layer_name='"number_name" LIKE "Ligne%"', ['qml'], ''''],
			LayerInfo(display_name='Cours d'eau (DGE)",'112_DWH_Gesreau', layer_name=''['qml'], 50, ''],
			LayerInfo(display_name='Traversé de localité (DGMR)', layer_name='112_DWH_TraverseLocalite'),
			LayerInfo(display_name='Axes de maintenance du réseau routier (DGMR)', layer_name='112_dwh_axe'),
			LayerInfo(display_name='Couverture du sol', '002_ITF_CS_Surface_CS', '"vd_genre" IN ("eau.cours_eau', layer_name='revetement_dur.route_chemin","revetement_dur.chemin_de_fer")'['qml'], 50, ''],
			LayerInfo(display_name='Réseaux dans les objet divers linéaires', '003_ITF_OD_Element_lineaire', layer_name='"vd_genre" IN ("eau_canalisee_souterraine","tunnel_passage_inferieur_galerie","pont_passerelle","quai","ru","sentier","ligne_aerienne_a_haute_tension","mat_antenne","conduite_forcee","voie_ferree,telepherique","telecabine_telesiege","telepherique_de_chantier","skilift","bac","axe")', ['qml'], ''''],
			LayerInfo(display_name='Réseaux dans les objet divers surfaciques', '003_ITF_OD_Element_surfacique', layer_name='"vd_genre" IN ("eau_canalisee_souterraine","tunnel_passage_inferieur_galerie","pont_passerelle","quai","ru","sentier","ligne_aerienne_a_haute_tension","mat_antenne","conduite_forcee","voie_ferree,telepherique","telecabine_telesiege","telepherique_de_chantier","skilift","bac","axe")', ['qml'], ''''],
			LayerInfo(display_name='DP', '006_ITF_BF_Bien_fonds', layer_name='"number" LIKE "DP%"', ['qml'], ''''],
			LayerInfo(display_name='Périmetre du lot",'112_itf_mise_a_jourrp', layer_name='', ['qml'], '''']
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
			LayerInfo(display_name='Point fixes dont les attributs ITF vs BDMO ne sont pas identiques', '115_itf_pfp_problemeattribut', layer_name=''['qml'], 50,'no'],
			LayerInfo(display_name='Points fixes en BDMO mais pas dans le fichier ITF', layer_name='115_bdmo_pfp_en_plus'),
			LayerInfo(display_name='Points fixes dans le fichier ITF mais pas en BDMO', layer_name='115_itf_pfp_en_plus', visible=False),
			LayerInfo(display_name='PFP-PFA3', layer_name='001_itf_pf_points_fixes'),
			LayerInfo(display_name='Précision planimétrique des points fixes', layer_name='115_itf_pfp'),
			LayerInfo(display_name='Périmetre du lot",'112_itf_mise_a_jourrp', layer_name='', ['qml'], '''']
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
			LayerInfo(display_name='Géometrie de limite de canton incorrecte (OGC)', '116_LigneCANT_OGC_fail', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,0', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='Géometrie de limite de commune incorrecte (OGC)', '116_LigneCOM_OGC_fail', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,0', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='Géometrie de limite de district incorrecte (OGC)', '116_LigneDIST_OGC_fail', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,0', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='point de limtes térritoriales manquant sous sommet de limite de commune', '116_PL_terr_manquant_sous_sommet_COM', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,0', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='sommet de limte de commune manquant sous point de limtes térritoriales', '116_Sommet_COM_manquant_sous_PL_terr', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,0', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='sommet de limte de commune manquant sous sommet de limite de canton', '116_sommetCOM_manquant_sous_sommet_CANT', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,0', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='sommet de limte decommune manquant sous sommet de limite de district', '116_sommetCOM_manquant_sous_sommet_Dist', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,0', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='point divergent entre les immeubles et la limite de commune', '103_VERIF_BF_COM_Point', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,255,0', QgsSymbolLayer.PropertySize:'2'}], ''''],
			LayerInfo(display_name='Sifflet entre les immeubles et la limite de commune', '103_VERIF_BF_COM_Surface', layer_name='', ['simple', {QgsSymbolLayer.PropertyFillColor: '255,0,0'}], ''''],
			LayerInfo(display_name='Point limite térritoriale",'008_itf_lt_point_limite_ter', layer_name='', ['qml'], ''''],
			LayerInfo(display_name='Limite commune', layer_name='008_itf_lt_limite_commune'),
			LayerInfo(display_name='Autre limite', layer_name='008_itf_lt_autre_limite'),
			LayerInfo(display_name='DDP",'006_ITF_BF_DDP', layer_name=''['qml'], 50, ''],
			LayerInfo(display_name='Biens fonds', '006_ITF_BF_Bien_fonds', layer_name=''['qml'], 50, '']
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