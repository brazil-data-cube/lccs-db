#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Command line interface for the Land Cover Classification System Database Model ."""
import os
import subprocess

import click
from flask import Flask
from flask.cli import FlaskGroup, with_appcontext
from sqlalchemy import text
from sqlalchemy_utils import create_database, database_exists

from lccs_db.models import db as _db

from .config import Config as config_infos
from .ext import LCCSDatabase


def create_app():
    """Create internal flask app."""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    LCCSDatabase(app)

    return app


def create_cli(create_app=None):
    """Define a wrapper to create Flask App in order to attach into flask click.

    Args:
         create_app (function) - Create app factory (Flask).
    """
    def create_cli_app(info):
        if create_app is None:
            info.create_app = None

            app = info.load_app()
        else:
            app = create_app()

        return app

    @click.group(cls=FlaskGroup, create_app=create_cli_app)
    def cli(*args, **params):
        pass

    return cli

cli = create_cli(create_app=create_app)


@cli.group()
@with_appcontext
def db():
    """Perform database migrations."""


@db.command()
@with_appcontext
def init_db():
    """Create database. Make sure the variable SQLALCHEMY_DATABASE_URI is set."""
    click.secho('Creating database {0}'.format(_db.engine.url),
                fg='green')
    if not database_exists(str(_db.engine.url)):
        create_database(str(_db.engine.url))

    with _db.session.begin_nested():
        click.secho('Creating schema if not exist {}...'.format(config_infos.ACTIVITIES_SCHEMA), fg='green')
        _db.session.execute("CREATE SCHEMA IF NOT EXISTS {}".format(config_infos.ACTIVITIES_SCHEMA))

    _db.session.commit()
