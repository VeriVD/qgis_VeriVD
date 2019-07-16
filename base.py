#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Connection class import
from spatialite import SpatialiteData

class BaseBiens_fonds(SpatialiteData):
	"""Class used to load ownership's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Base - Biens fonds"
		#set layer's parameter in a dict list
		self.infoLayer = 	(
							[u'Numéros des DDP','006_ITF_BF_Pos_DDP','',['qml'],'',''],
							[u'Numéros des biens fonds','006_ITF_BF_Pos_Bien_fonds','',['qml'],'',''],
							[u'Point limite','006_ITF_BF_Point_limite','',['qml'],'',''],
							[u"DDP",'006_ITF_BF_DDP','',['qml'],'',''],
							[u'Biens fonds','006_ITF_BF_Bien_fonds','',['qml'],'','']
							)

class BaseCouverture_du_sol(SpatialiteData):
	"""Class used to load land cover's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Base - Couverture du sol"    
		self.infoLayer = 	(
							[u'Nom et numéro CS','002_ITF_CS_Pos_Surface_CS','',['qml'],'',''],
							[u"Point particulier CS",'002_ITF_CS_Point_particulier','',['qml'],'',''],
							[u'Surface CS','002_ITF_CS_Surface_CS','',['qml'],'',''],
							[u'Bâtiment','002_ITF_CS_Surface_CS','"type" = "batiment"',['simple',{'color':'255,210,210','border_color':'black'}],'','']
							)

class BaseObjets_divers(SpatialiteData):
	"""Class used to load single object's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Base - Objets divers"    
		self.infoLayer = 	(
							[u'OD linéaire','003_ITF_OD_Element_lineaire','',['qml'],'',''],
							[u'OD surfacique','003_ITF_OD_Element_surfacique','',['qml'],'',''],
							[u"OD point particulier",'003_ITF_OD_Point_particulier','',['qml'],'',''],
							[u"OD Nom et Numéro ligne",'003_ITF_OD_Pos_Element_lineaire','',['qml'],'',''],
							[u"OD Nom et Numéro surface",'003_ITF_OD_Pos_Element_surfacique','',['qml'],'','']
							)
							
class BaseNomenclature(SpatialiteData):
	"""Class used to load local names's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Base - Nomenclature"
		self.infoLayer = 	(
							[u'Lieux dits texte','005_itf_no_pos_lieudit','',['qml'],'',''],
							[u'Nom local texte','005_itf_no_posnom_local','',['qml'],'',''],
							[u'Nom local','005_ITF_NO_Nom_local','',['randomCategorized',{'field':'name'}],'','']
							)
							
class BaseConduite(SpatialiteData):
	"""Class used to load local names's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Base - Conduite"
		self.infoLayer = 	(
							[u'CO Conduite','007_itf_co_element_conduite','',['qml'],'',''],
							[u'CO Conduite Nom','007_itf_co_poselement_conduite','',['qml'],'','']
							)
							
class BasePoints_fixes(SpatialiteData):
	"""Class used to load local names's layers"""
	def __init__(self, pathSQliteDB):
		self.groupName = u"Base - Points fixes"
		SpatialiteData.__init__(self, pathSQliteDB)
		self.infoLayer = 	[
							[u'PFP-PFA3','001_itf_pf_points_fixes','',['qml'],'',''],
							]
							
class BaseAltimetrie(SpatialiteData):
	"""Class used to load local names's layers"""
	def __init__(self, pathSQliteDB):
		self.groupName = u"Base - Courbes de niveau"
		SpatialiteData.__init__(self, pathSQliteDB)
		self.infoLayer = 	[
							[u'Courbes de niveau','004_itf_al_courbes_de_niveau','',['qml'],'','']
							]

class BaseRepartition_des_plans(SpatialiteData):
	"""Class used to load local names's layers"""
	def __init__(self, pathSQliteDB):
		self.groupName = u"Base - Répartition des plans"
		SpatialiteData.__init__(self, pathSQliteDB)
		self.infoLayer = 	[
							[u'Plan','105_itf_rp','',['qml'],'','']
							]

class BaseAdresses_des_batiments(SpatialiteData):
	"""Class used to load local names's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Base - Adresses des bâtiments"
		self.infoLayer = 	(
							[u"Numéro d'entrée",'009_itf_bat_posentree_batiment','',['qml'],'',''],
							[u'Nom de localisation','009_itf_bat_posnom_localisation','',['qml'],'',''],
							[u'Point de départ des tronçons','009_itf_bat_point_depart','',['qml'],'',''],
							[u'Entrée des bâtiments','009_itf_bat_entree_batiment','',['qml'],'',''],
							[u'Tronçon de rue','009_itf_bat_troncon_rue','',['qml'],'','']
							)

class BaseLimites_territoriales(SpatialiteData):
	"""Class used to load local names's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Base - Limites térritoriales"
		self.infoLayer = 	(
							[u"Point limite térritoriale",'008_itf_lt_point_limite_ter','',['qml'],'',''],
							[u'Limite commune','008_itf_lt_limite_commune','',['qml'],'',''],
							[u'Autre limite','008_itf_lt_autre_limite','',['qml'],'',''],
							)

class BaseTous_les_topics(SpatialiteData):
	"""Class used to load local names's layers"""
	def __init__(self, pathSQliteDB):
		SpatialiteData.__init__(self, pathSQliteDB)
		self.groupName = u"Base - Tous les topics"
		self.infoLayer = 	(
							[u'Nom et numéro CS','002_ITF_CS_Pos_Surface_CS','',['qml'],'',''],
							[u'Numéros des DDP','006_ITF_BF_Pos_DDP','',['qml'],'',''],
							[u'Numéros des biens fonds','006_ITF_BF_Pos_Bien_fonds','',['qml'],'',''],
							[u'CO Conduite Nom','007_itf_co_poselement_conduite','',['qml'],'',''],
							[u"Numéro d'entrée",'009_itf_bat_posentree_batiment','',['qml'],'',''],
							[u"OD Nom et Numéro ligne",'003_ITF_OD_Pos_Element_lineaire','',['qml'],'',''],
							[u"OD Nom et Numéro surface",'003_ITF_OD_Pos_Element_surfacique','',['qml'],'',''],
							[u'Nom de localisation','009_itf_bat_posnom_localisation','',['qml'],'',''],
							[u'Lieux dits texte','005_itf_no_pos_lieudit','',['qml'],'',''],
							[u'Nom local texte','005_itf_no_posnom_local','',['qml'],'',''],
							[u'Nom local','005_ITF_NO_Nom_local','',['randomCategorized',{'field':'name'}],50,'no'],
							[u'PFP-PFA3','001_itf_pf_points_fixes','',['qml'],'',''],
							[u'Point limite','006_ITF_BF_Point_limite','',['qml'],'',''],
							[u"Point particulier CS",'002_ITF_CS_Point_particulier','',['qml'],'',''],
							[u"Point limite térritoriale",'008_itf_lt_point_limite_ter','',['qml'],'',''],
							[u'OD linéaire','003_ITF_OD_Element_lineaire','',['qml'],'',''],
							[u'OD surfacique','003_ITF_OD_Element_surfacique','',['qml'],'',''],
							[u"OD point particulier",'003_ITF_OD_Point_particulier','',['qml'],'',''],
							[u'Point de départ des tronçons','009_itf_bat_point_depart','',['qml'],'',''],
							[u'Entrée des bâtiments','009_itf_bat_entree_batiment','',['qml'],'',''],
							[u'Tronçon de rue','009_itf_bat_troncon_rue','',['qml'],'',''],
							[u'CO Conduite','007_itf_co_element_conduite','',['qml'],'',''],
							[u'Courbes de niveau','004_itf_al_courbes_de_niveau','',['qml'],'','no'],
							[u'Plan','105_itf_rp','',['qml'],'',''],
							[u'Limite commune','008_itf_lt_limite_commune','',['qml'],'',''],
							[u'Autre limite','008_itf_lt_autre_limite','',['qml'],'',''],
							[u"DDP",'006_ITF_BF_DDP','',['qml'],'',''],
							[u'Biens fonds','006_ITF_BF_Bien_fonds','',['qml'],'',''],
							[u'Surface CS','002_ITF_CS_Surface_CS','',['qml'],'',''],
							)