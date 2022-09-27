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

"""Config test fixtures."""

import subprocess

import pytest
from flask import Flask


@pytest.fixture
def app():
    """Flask application fixture."""
    app = Flask(__name__)

    return app


@pytest.fixture
def db():
    """Return the SQLAlchemy database instance."""
    from lccs_db.models import db

    return db


def pytest_sessionstart(session):
    """Load LCCS-DB and prepare database environment."""
    for command in ['init', 'create-namespaces', 'create-extension-hstore', 'create-schema', 'load-scripts']:
        subprocess.call(f'lccs-db db {command}', shell=True)


def pytest_sessionfinish(session, exitstatus):
    """Destroy database created."""
    subprocess.call(f'lccs-db db destroy --force', shell=True)
