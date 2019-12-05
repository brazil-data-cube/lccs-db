#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Command line interface for the Land Cover Classification System Database Model ."""

import click

@click.group()
def cli():
    """LCCSDM on command line."""
    pass


@click.command()
@click.option('--user', default=None, help='PostgreSQL user.')
@click.option('--host', default=None, help='PostgreSQL host.')
@click.option('--password', default=None, help='PostgreSQL password.')
@click.option('--port', default=None, help='PostgreSQL port.')
@click.option('--db_name', default=None, help='PostgreSQL database name.')

def db_connection(url):
    """Set database connection URL."""

    click.echo("ok")


cli.add_command(db_connection)