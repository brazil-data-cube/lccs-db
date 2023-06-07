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

"""Unit-test for lccs_db."""

import subprocess
import sys

from click.testing import CliRunner
from flask.cli import ScriptInfo

import pytest
from lccs_db.cli import cli
from lccs_db import LCCSDatabase

from bdc_db.config import SQLALCHEMY_DATABASE_URI

from sqlalchemy_utils.functions import database_exists


def test_basic_cli():
    """Test basic cli usage."""
    res = CliRunner().invoke(cli)
    
    assert res.exit_code == 0


def test_cli_module():
    """Test the LCCS-DB invoked as a module."""
    res = subprocess.call(f'{sys.executable} -m lccs_db', shell=True)
    
    assert res == 0


def test_load_system_file():
    """Test the load classification system."""
    res = subprocess.call(
        f'{sys.executable} -m lccs_db db load-file --file tests/scripts/test-class-system.sql', shell=True)

    assert res == 0