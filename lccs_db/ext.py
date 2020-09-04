#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Defines flask extension module for the Land Cover Classification System Database Model."""
from bdc_db.ext import BrazilDataCubeDB
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .cli import cli
from .models.base import db as _db


class LCCSDatabase:
    """LCCSDB extension."""

    # Reference to BrazilDataCubeDB app instance
    _db_ext = None

    def __init__(self, app=None):
        """Initialize the lccs_db extension.

        Args:
            app: Flask application
            kwargs: Optional arguments (not used).
        """
        if app:
            self.init_app(app)

    def init_app(self, app: Flask):
        """Initialize Flask application instance.

        Args:
            app: Flask application
            kwargs: Optional arguments (not used).
        """
        self._db_ext = BrazilDataCubeDB(app)
        app.extensions['lccs-db'] = self

        app.cli.add_command(cli)

    @property
    def db(self) -> SQLAlchemy:
        """Retrieve instance Flask-SQLALchemy instance.

        Notes:
            Make sure to initialize the `BDCCatalog` before.
        """
        return _db