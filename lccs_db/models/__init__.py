#
# This file is part of LCCS-DB.
# Copyright (C) 2022 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#

"""Python Land Cover Classification System Database Model."""

from .base import db
from .class_mapping import ClassMapping
from .luc_class import ClassesView, LucClass
from .luc_classification_system import (ClassificationSystemSRC,
                                        LucClassificationSystem)
from .style_formats import StyleFormats
from .styles import Styles

__all__ = ('db', 'LucClass', 'LucClassificationSystem', 'ClassMapping',
           'StyleFormats', 'Styles', 'ClassesView',)
