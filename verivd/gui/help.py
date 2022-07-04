#!/usr/bin/env python
# -*- coding: utf-8 -*-

WEB_SPATIALITE = 'https://www.gaia-gis.it/fossil/libspatialite/index'
WEB_MOPUBLIC = 'https://www.cadastre.ch/fr/services/service/mopublic.html'
WEB_NORMEVD = 'https://dwa.vd.ch/PROD/DINF/publicationdinf1_p.nsf/normesformulaires?SearchView&Query='
REQUETE = '(FIELD%20TitreNorme%20CONTAINS%20{})'
WEB_CHECKER = 'https://www.vd.ch/themes/territoire-et-construction/informations-sur-le-territoire/mensuration-officielle/informations-aux-bureaux-de-geometres/checker-interlis/'
WEB_6052 = "https://www.vd.ch/fileadmin/user_upload/organisation/dinf/sit/fichiers_pdf/VeriVD/6052_VeriVD_infoV2_projet_20210423.pdf"

MESSAGE_FICHIER = """Le fichier .sqlite qui alimente ce plugin, contient une base de données spatiale au format <a href='{}'>spatialite</a>. 
Ce fichier est generée à l'OIT sur la base d'un fichier interlis décrit selon le modèle MD01MOVDMN95.""".format(WEB_SPATIALITE)

MESSAGE_BASE = """Cet onglet permet le chargement des couches de bases. Celles-ci sont inspirées du modèle simplifé de la mensuration officielle: <a href='{}'>MO-Public</a>. 
Quelques éléments importants issues du  <a href='{}'>modèle officiel</a>  ont éé ajoutés à ces données avec un 'préfixe VD'. 
La symbologie provient de la <a href='{}'>norme vaudoise 6411</a>""".format(WEB_MOPUBLIC, WEB_NORMEVD + REQUETE.format('6021'), WEB_NORMEVD + REQUETE.format('6411'))

MESSAGE_ILIVALIDATOR = """A défnir"""

MESSAGE_CHECKER = """Cet onglet permet le chargement des données issues du <a href='{}'>checker interlis vaudois</a>. 
Pour plus d'informations, veuiller consulter la page web s'y référant.""".format(WEB_CHECKER)

MESSAGE_VERIF = """Cet onglet permet le chargement des données des tests de vérification dévelopés en interne à l'OIT (office de l'information sur le territoire). Des explications relatives à chacun de ces tests sont disponnible dans la fiche <a href='{}'>6052</a>.""".format(WEB_6052)