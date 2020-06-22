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


class VeriLayer:
    def __init__(self, name: str, display_name: str = None):
        self._name = name
        self._display_name = display_name or name
        self._loaded = False

    @property
    def name(self):
        return self._name

    @property
    def display_name(self):
        return self._display_name

    @property
    def loaded(self):
        return self._loaded

    @loaded.setter
    def loaded(self, value: bool):
        self._loaded = value
        # TODO load/unload