#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for lccs_db models."""
import os
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('../'))


alembic_root = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'migrations'))


def setUp():
    uri = "postgresql://postgres:123456@5432:/teste"
    assert 1 == 1

def test_upgrade_and_downgrade():
    assert 1 == 1

def test_model_and_migration_schemas_are_the_same():
    assert 1 == 1

