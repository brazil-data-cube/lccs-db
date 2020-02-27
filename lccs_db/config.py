#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Database Model ."""

import os

CURRENT_DIR = os.path.dirname(__file__)


class Config:
    """Define common config along contexts."""
    ACTIVITIES_SCHEMA = os.environ.get('ACTIVITIES_SCHEMA', 'lccs')