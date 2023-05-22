"""
/***************************************************************************
 VeriVD
                                 A QGIS plugin
 Vérification des mensurations vaudoises
                             -------------------
        begin                : 2018-11-15
        copyright            : (C) 2018 by FSN/OIT
        email                : fabien.simon@vd.ch
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def classFactory(iface):
    from verivd.gui.veri_vd_plugin import VeriVD

    return VeriVD(iface)
