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
import mimetypes

from .ext import LCCSDatabase
from .version import __version__

mimetypes.init()
mimetypes.add_type("application/xml", ".qml", True)
mimetypes.add_type("application/vnd.ogc.sld+xml", ".sld", True)


__all__ = ('__version__', 'LCCSDatabase',)
