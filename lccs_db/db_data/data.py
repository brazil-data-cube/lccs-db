#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Python Land Cover Classification System Database Model."""

import os.path

def load_data(file_path):

    with open(file_path) as f:
        data = f.read()

    return data

def load_dbdata():

    module_path = os.path.dirname(os.path.abspath(__file__))

    sql = load_data(os.path.join(module_path, 'sql_insert.sql'))

    return sql