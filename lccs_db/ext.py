#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Defines flask extension module for the Land Cover Classification System Database Model."""
import os

import pkg_resources
from flask import Flask, current_app
from flask_alembic import Alembic
from sqlalchemy.orm import configure_mappers

from .models import db


def include_object(object, name, type_, reflected, compare_to):
    """Ignores the tables in 'exclude_tables'."""
    exclude_tables = current_app.config.get('ALEMBIC_EXCLUDE_TABLES', [])
    return not (type_ == "table" and name in exclude_tables)


class LCCSDatabase:
    """Land Cover Classification Model extension."""

    def __init__(self, app=None, **kwargs):
        """Extension initialization."""
        self.alembic = Alembic(run_mkdir=True, command_name='alembic')

        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app: Flask, **kwargs):
        """Initialize flask application object."""
        self.init_db(app, **kwargs)

        script_location = pkg_resources.resource_filename(
            'lccs_db', 'alembic'
        )

        version_locations = [
            (base_entry.name, pkg_resources.resource_filename(
                base_entry.module_name, os.path.join(*base_entry.attrs,)
            )) for base_entry in pkg_resources.iter_entry_points(
                'lccs_db.alembic'
            )
        ]

        # Remove duplicated lccs_db version_locations since
        # the lccs-db is also registered on setup entry_points
        if ('lccs_db', script_location) in version_locations:
            version_locations.remove(('lccs_db', script_location))

        # Defines entrypoints for dynamically model loading
        app.config.setdefault('ALEMBIC', {
            'script_location': script_location,
            'version_locations': version_locations,
        })

        app.config.setdefault('ALEMBIC_EXCLUDE_TABLES', ['spatial_ref_sys'])

        handler_include_table = kwargs.get('include_object', include_object)

        app.config.setdefault('ALEMBIC_CONTEXT', {
            'compare_type': True,
            'include_schemas': True,
            'include_object': handler_include_table,

        })

        # Initialize Flask-Alembic
        self.alembic.init_app(app, **kwargs)

        app.extensions['lccs-db'] = self

    def init_db(self, app: Flask, entry_point_group: str='lccs_db.models', **kwargs):
        """Initialize Flask-SQLAlchemy extension.

        Args:
            app - Flask application
            entry_point_group - Entrypoint definition to load models
            **kwargs - Optional arguments to Flask-SQLAlchemy.
        """
        # Setup SQLAlchemy
        app.config.setdefault(
            'SQLALCHEMY_DATABASE_URI',
            os.environ.get('SQLALCHEMY_DATABASE_URI')
        )

        app.config.setdefault(
            'SQLALCHEMY_TRACK_MODIFICATIONS',
            os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
        )
        app.config.setdefault('SQLALCHEMY_ECHO', False)

        # Initialize Flask-SQLAlchemy extension.
        database = kwargs.get('db', db)
        database.init_app(app)

        # Loads all models
        if entry_point_group:
            for base_entry in pkg_resources.iter_entry_points(entry_point_group):
                base_entry.load()

        # All models should be loaded by now.
        configure_mappers()
