#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test configuration."""

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
