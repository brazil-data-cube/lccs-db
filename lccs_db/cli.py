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

import sqlalchemy
from sqlalchemy import text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import create_database, database_exists

import click
from lccs_db.data import load_dbdata


class Config:
    """A simple decorator class for command line options."""

    def __init__(self):
        """Initialization of Config decorator."""
        self.uri = None
        self.engine = None
        self.maker = None
        self.DBSession = None
        self.session = None

    def execute(self, sql_query):
        """Execute query of Config decorator."""
        with self.engine.connect() as conn:
            conn.execute(text(sql_query))


pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--user', type=click.STRING, default=None, help='PostgreSQL user.')
@click.option('--host', type=click.STRING, default='localhost', help='PostgreSQL host.')
@click.option('--password', prompt=True, hide_input=True, default=None, help='PostgreSQL password.')
@click.option('--port', type=click.INT, default=5432, help='PostgreSQL port.')
@click.option('--db_name', type=click.STRING, default=None, help='PostgreSQL database name.')
@pass_config
def cli(config, user, host, password, port, db_name):
    """LCCSDM on command line."""
    config.uri = "postgresql://{}:{}@{}:{}/{}".format(user, password, host, port, db_name)

    config.engine = sqlalchemy.create_engine(config.uri)

    Session = scoped_session(sessionmaker(bind=config.engine))

    config.session = Session()

@cli.command()
@pass_config
def init_db(config):
    """Initial Database."""
    if not database_exists(config.engine.url):
        create_database(config.engine.url)

    click.echo("DB Create!")

@cli.command()
@pass_config
def init_alembic(config):
    """Initial Alembic."""
    env = os.environ.copy()
    env["PYTHONPATH"] = "."
    env["PATH"] = "{}:{}".format(os.path.expanduser("~/.local/bin"), env["PATH"])
    env["SQLALCHEMY_DATABASE_URI"] = config.uri

    sp = subprocess.Popen(["alembic", "upgrade", "head"], env=env)

    if (sp.wait() != 0):
        raise ValueError("Alembic upgrade head error ")

@cli.command()
@click.option('--ifile', type=click.File('r'),
              help='A SQL input file for insert.',
              required=False)
@pass_config
def insert_db(config, ifile):
    """Insert Database."""
    if ifile is not None:
        sql = ifile.read()

    else:
        sql = load_dbdata()

    config.execute(sql)

    click.echo("Insert Data ok!")
