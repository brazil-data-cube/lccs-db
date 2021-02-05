#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for extension BDC-Catalog."""

from lccs_db import LCCSDatabase


def test_ext_creation(app):
    ext = LCCSDatabase(app)

    assert app.extensions['lccs-db'] == ext