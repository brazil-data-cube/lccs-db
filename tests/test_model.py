#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2021 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Unit-test for models of LCCS-DB."""
import pytest

from lccs_db import LCCSDatabase
from lccs_db.models import LucClassificationSystem


@pytest.fixture
def db(app):
    ext = LCCSDatabase(app)

    yield ext.db


@pytest.fixture
def test_classification_system():
    """Test create a classification system."""
    system = LucClassificationSystem(
        name="Classification-System-Test",
        authority_name="BDC",
        description="Description",
        version="1.0"
    )
    with db.session.begin_nested():
        db.session.add(system)
        db.session.commit()

    assert system.id

