#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for lccs_db."""

import subprocess

from click.testing import CliRunner

from lccs_db.cli import cli


def test_cli_basic():
    """Test basic cli usage."""
    res = CliRunner().invoke(cli)

    assert res.exit_code == 0


def test_database_creation():
    """Test cli database creation."""
    exit_status = subprocess.call('lccs_db db init', shell=True)

    assert exit_status == 0
