#
# This file is part of Land Cover Classification System Database Model..
# Copyright (C) 2021 INPE.
#
# Land Cover Classification System Database Model. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Utility for Land Cover Classification System Database Model."""
import mimetypes


def validate_mimetypes(style_file):
    """Return allowed files.

    :param style_file: Full style file name.
    :type style_file: string
    """
    extensions = mimetypes.guess_type(style_file)

    return extensions[0]
