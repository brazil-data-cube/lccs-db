#
# This file is part of LCCS-DB.
# Copyright (C) 2022 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#

"""Utility for Land Cover Classification System Database Model."""
import mimetypes
from functools import wraps

from flask import abort, request

from .config import Config
from .models.base import translation_hybrid


def set_locale(locale: str):
    """Update the location."""
    translation_hybrid.current_locale = locale


def language(language=None, required=False):
    """Decorate for locale."""
    def _language(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            support_language = [Config.I18N_LANGUAGES['current_locale'][0],
                                Config.I18N_LANGUAGES['default_locale'][0]]

            language_str = request.headers['language'] if request.headers.get('language') else \
                            request.args.get('language')
            if language_str:
                if language_str not in support_language:
                    abort(403, 'Language not supported!')
                set_locale(language_str)
            return func(*args, **kwargs)
        return wrapped
    return _language


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
