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

"""Land Cover Classification System Database Model ."""

import os

CURRENT_DIR = os.path.dirname(__file__)


class Config:
    """Define common config along contexts."""

    LCCS_SCHEMA_NAME = os.environ.get('LCCS_SCHEMA_NAME', 'lccs')
    I18N_LANGUAGES = {'current_locale': ('en', 'English'), 'default_locale': ('pt-br', 'Brazilian Portuguese')}
