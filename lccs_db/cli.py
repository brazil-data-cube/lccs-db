#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Command-Line Interface for the Land Cover Classification System Database Model ."""
import click
from bdc_db.cli import cli
from bdc_db.db import db as _db
from flask.cli import with_appcontext

from .models import LucClassificationSystem, StyleFormats, Styles
from .utils import validate_mimetypes


@cli.group()
def lccs():
    """More lccs database commands."""


@lccs.command()
@with_appcontext
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.option('--system_id', type=click.STRING, required=True, help='The classification system id (name).')
@click.option('--version', type=click.STRING, required=True, help='The classification system id (name).')
@click.option('--style_format_id', type=click.STRING, required=True, help='The style format.')
@click.option('-f', '--file', type=click.File('rb'),
              help='A style file for insert.',
              required=True)
def insert_style(verbose, file, system_id, version, style_format_id):
    """Insert style of classification system."""
    style_file = file.read()

    mime_type = validate_mimetypes(file.name)

    if verbose:
        click.secho(f'Insert {style_format_id} style for {system_id}..', bold=True, fg='yellow')

    system = LucClassificationSystem.get(name=system_id, version=version)

    style_format = StyleFormats.get(name=style_format_id)

    style_infos = dict(
        class_system_id=system.id,
        style_format_id=style_format.id,
        mime_type=mime_type,
        style=style_file
    )

    with _db.session.begin_nested():
        style = Styles(**dict(style_infos))

        _db.session.add(style)

    _db.session.commit()

    click.secho(f'File {style_format_id} loaded!', bold=True, fg='green')


def main(as_module=False):
    """Define a main function for executing the module."""
    # TODO omit sys.argv once https://github.com/pallets/click/issues/536 is fixed
    import sys
    cli.main(args=sys.argv[1:], prog_name="python -m lccs_db" if as_module else None)
