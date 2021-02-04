#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
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
    """Test the BDCCatalog invoked as a module."""
    res = subprocess.call(f'{sys.executable} -m lccs_db', shell=True)

    assert res == 0
