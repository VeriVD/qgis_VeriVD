#!/usr/bin/env python

WEB_GEOPACKAGE = "https://www.geopackage.org/"
WEB_MOPUBLIC = "https://www.cadastre.ch/fr/services/service/mopublic.html"
WEB_NORMEVD = "https://dwa.vd.ch/PROD/DINF/publicationdinf1_p.nsf/normesformulaires?SearchView&Query="
REQUETE = "(FIELD%20TitreNorme%20CONTAINS%20{})"
WEB_CHECKER = "https://www.vd.ch/themes/territoire-et-construction/informations-sur-le-territoire/mensuration-officielle/informations-aux-bureaux-de-geometres/checker-interlis/"
WEB_ILIVALIDATOR = "https://www.interlis.ch/fr/downloads/ilivalidator"
WEB_6052 = "https://www.vd.ch/fileadmin/user_upload/organisation/dinf/sit/fichiers_pdf/VeriVD/6052_VeriVD_infoV2_projet_20210423.pdf"

MESSAGE_FICHIER = f"""Le fichier .gpkg qui alimente ce plugin, contient une base de données spatiale au format <a href='{WEB_GEOPACKAGE}'>geopackage</a>.
 Ce fichier est generée à la DCG sur la base d'un fichier interlis décrit selon le modèle MD01MOVDMN95."""

MESSAGE_BASE = """Cet onglet permet le chargement des couches de bases. Celles-ci sont inspirées du modèle simplifé 
de la mensuration officielle: <a href='{}'>MO-Public</a>. Quelques éléments importants issues du  <a href='{}'>modèle 
officiel</a>  ont éé ajoutés à ces données avec un 'préfixe VD'. La symbologie provient de la <a href='{}'>norme 
vaudoise 6411</a>""".format(
    WEB_MOPUBLIC,
    WEB_NORMEVD + REQUETE.format("6021"),
    WEB_NORMEVD + REQUETE.format("6411"),
)

MESSAGE_ILIVALIDATOR = f"""Cet onglet permet le chargement des données issues de <a href='{WEB_ILIVALIDATOR}'>l'ilivalidator interlis 
</a>. Pour plus d'informations, veuiller consulter la page web s'y référant. """

MESSAGE_CHECKER = f"""Cet onglet permet le chargement des données issues du <a href='{WEB_CHECKER}'>checker interlis 
</a>. Pour plus d'informations, veuiller consulter la page web s'y référant. """

MESSAGE_VERIF = f"""Cet onglet permet le chargement des données des tests de vérification dévelopés en interne à 
la DCG (direction du cadastre et de la géoinformation). Des explications relatives à chacun de ces tests sont disponnibles 
dans la fiche <a href='{WEB_6052}'>6052</a>. """
