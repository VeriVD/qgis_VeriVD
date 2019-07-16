#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Aide:
	"""Class used to load the help"""
	def __init__(self):
		self.webSpatialite = 'https://www.gaia-gis.it/fossil/libspatialite/index'
		self.webMoPublic = 'https://www.cadastre.ch/fr/services/service/mopublic.html'
		self.webNormeVD = 'https://dwa.vd.ch/PROD/DINF/publicationdinf1_p.nsf/normesformulaires?SearchView&Query='
		self.requete = '(FIELD%20TitreNorme%20CONTAINS%20{})'
		self.webChecker = 'https://www.vd.ch/themes/territoire-et-construction/informations-sur-le-territoire/mensuration-officielle/informations-aux-bureaux-de-geometres/checker-interlis/'

		self.messageFichier = """Le fichier .sqlite qui alimente ce plugin, contient une base de données spatiale au format <a href='{}'>spatialite</a>. 
Ce fichier est generée à l'OIT sur la base d'un fichier interlis décrit selon le modèle MD01MOVDMN95.""".format(self.webSpatialite)
		self.messageBase = """Cet onglet permet le chargement des couches de bases. Celles-ci sont inspirées du modèle simplifé de la mensuration officielle: <a href='{}'>MO-Public</a>. 
Quelques éléments importants issues du  <a href='{}'>modèle officiel</a>  ont été ajoutés à ces données avec un 'préfixe VD'. 
La symbologie provient de la <a href='{}'>norme vaudoise 6411</a>""".format(self.webMoPublic, self.webNormeVD+self.requete.format('6021'), self.webNormeVD+self.requete.format('6411'))
		self.messageIliValidator = """A défnir"""
		self.messageChecker = """Cet onglet permet le chargement des données issues du <a href='{}'>checker interlis vaudois</a>. 
Pour plus d'informations, veuiller consulter la page web s'y reférant.""".format(self.webChecker)
		self.messageVerif = """Cet onglet permet le chargement des données des tests de vérification dévelopés en interne à l'OIT (office de l'information sur le térritoire). Des explications relatives à chacun de ces tests sont disponnible dans la norme <a href='{}'>vérification des mensurations</a>.""".format(self.webChecker)