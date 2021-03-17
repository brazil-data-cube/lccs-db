#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
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
    for command in ['init', 'create-namespaces', 'create-schema', 'load-scripts']:
        subprocess.call(f'lccs-db db {command}', shell=True)


def pytest_sessionfinish(session, exitstatus):
    """Destroy database created."""
    subprocess.call(f'lccs-db db destroy --force', shell=True)
