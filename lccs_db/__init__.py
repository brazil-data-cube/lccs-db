#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Python Client Library for Land Cover Classification System Database Model."""

from lccs_db.model import base, luc_classification_system

from .version import __version__

__all__ = ('__version__', 'base', 'luc_classification_system',)