#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2021 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Unit-test for mimetypes."""

from lccs_db.utils import get_mimetype, get_extension


def test_get_type():
    type = get_mimetype('test-type.sld')
    assert type == 'application/vnd.ogc.sld+xml'


def test_get_extension():
    ext = get_extension('application/vnd.ogc.sld+xml')
    assert ext == '.sld'
