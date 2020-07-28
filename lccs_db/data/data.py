#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Python Land Cover Classification System Database Model."""

from pkg_resources import resource_string


def load_data(file_path):
    """Load file."""
    with open(file_path) as f:
        data = f.read()

    return data

def load_dbdata():
    """Load data."""
    resource_package = __name__

    resource_path = 'default_class_systems.sql'

    sql = resource_string(resource_package, resource_path).decode('utf-8')

    return  sql
