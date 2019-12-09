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

def alembic_migration(url):
    """LCCSDM on command line."""
    env = os.environ.copy()
    env["PYTHONPATH"] = "."
    env["PATH"] = "{}:{}".format(os.path.expanduser("~/.local/bin"), env["PATH"])

    sp = subprocess.Popen(["alembic", "upgrade", "head"], env={"SQLALCHEMY_DATABASE_URI": url})

    sp.wait()


@click.group()
def cli():
    """LCCSDM on command line."""
    pass


@click.command()
@click.option('--user', default=None, help='PostgreSQL user.')
@click.option('--host', default=None, help='PostgreSQL host.')
@click.option('--password', prompt=True, hide_input=True,default=None, help='PostgreSQL password.')
@click.option('--port', default=None, help='PostgreSQL port.')
@click.option('--db_name', default=None, help='PostgreSQL database name.')
def run_migration(user, host, password, port, db_name):
    """Set database connection URL."""
    url = "postgresql://postgres:{}@{}:{}/{}".format(password, host, port, db_name)

    alembic_migration(url)



cli.add_command(run_migration)
