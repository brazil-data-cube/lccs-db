#
# This file is part of Land Cover Classification System Database Model..
# Copyright (C) 2021 INPE.
#
# Land Cover Classification System Database Model. is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Utility for Land Cover Classification System Database Model."""
import mimetypes


def get_mimetype(style_file):
    """Return mimetype of a file.

    :param style_file: The style file system path.
    :type style_file: string
    """
    extensions = mimetypes.guess_type(style_file)
    
    return extensions[0]


def get_extension(mimetype):
    """Return the last the extensions for a file based on its MIME type.
    
    :param mimetype: The MIME type.
    :type mimetype: string
    """
    extensions = mimetypes.guess_all_extensions(mimetype)
    return extensions[-1]
