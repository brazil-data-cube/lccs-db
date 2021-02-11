#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Python Land Cover Classification System Database Model."""
import mimetypes

from .ext import LCCSDatabase
from .version import __version__

mimetypes.init()
mimetypes.add_type("application/xml", ".qml", True)
mimetypes.add_type("application/vnd.ogc.sld+xml", ".sld", True)


__all__ = ('__version__', 'LCCSDatabase',)
