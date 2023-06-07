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

"""Command-Line Interface for the Land Cover Classification System Database Model ."""
import click
from bdc_db.cli import cli, db
from bdc_db.db import db as _db
from flask.cli import with_appcontext

from .models import LucClassificationSystem, StyleFormats, Styles
from .utils import get_mimetype


@cli.group()
def lccs():
    """More lccs database commands."""


@db.command()
@with_appcontext
def create_extension_hstore():
    """Enable the HSTORE extension in the database."""
    click.secho(f'Creating extension hstore...', bold=True, fg='yellow')

    with _db.session.begin_nested():
        _db.session.execute('CREATE EXTENSION IF NOT EXISTS hstore')
    _db.session.commit()

    click.secho('Extension created!', bold=True, fg='green')


@lccs.command()
@with_appcontext
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.option('--system_name', type=click.STRING, required=True, help='The classification system name.')
@click.option('--system_version', type=click.STRING, required=True, help='The classification system version.')
@click.option('--style_format_name', type=click.STRING, required=True, help='The style format name.')
@click.option('-f', '--file', type=click.File('rb'),
              help='A style file for insert.',
              required=True)
def insert_style(verbose, file, system_name, system_version, style_format_name):
    """Insert style of classification system."""
    style_file = file.read()

    mime_type = get_mimetype(file.name)

    if verbose:
        click.secho(f'Insert {style_format_name} style for {system_name}..', bold=True, fg='yellow')

    system = LucClassificationSystem.get(name=system_name, version=system_version)

    style_format = StyleFormats.get(name=style_format_name)

    style_infos = dict(
        classification_system_id=system.id,
        style_format_id=style_format.id,
        mime_type=mime_type,
        style=style_file
    )

    with _db.session.begin_nested():
        style = Styles(**dict(style_infos))

        _db.session.add(style)

    _db.session.commit()

    click.secho(f'File {style_format_name} loaded!', bold=True, fg='green')


def main(as_module=False):
    """Define a main function for executing the module."""
    # TODO omit sys.argv once https://github.com/pallets/click/issues/536 is fixed
    import sys
    cli.main(args=sys.argv[1:], prog_name="python -m lccs_db" if as_module else None)
