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


from verivd.core.symbolgy_type import SymbologyType


class LayerInfo(object):
	def __init__(
			self,
			display_name: str,
			layer_name: str,
			symbology_type: SymbologyType = SymbologyType.QML,
			symbology_properties: dict = {},
			symbology_data_defined_properties: dict = {},
			category_field = None,
			sql_request: str = '',
			visibility: bool = True,
			opacity: float = 1,
			control_layer: bool = False,
	):
		"""

		:param display_name:
		:param layer_name:
		:param symbology_type:
		:param symbology_properties:
		:param symbology_data_defined_properties:
		:param category_field:
		:param sql_request:
		:param visibility:
		:param opacity:
		:param control_layer: if True, the plugin will report if no control layer has been loaded (saying no errors have been encountered)
		"""
		self.display_name = display_name
		self.layer_name = layer_name
		self.sql_request = sql_request
		self.symbology_type = symbology_type
		self.symbology_properties = symbology_properties
		self.symbology_data_defined_properties = symbology_data_defined_properties
		self.category_field = category_field
		self.opacity = opacity
		self.visibility = visibility