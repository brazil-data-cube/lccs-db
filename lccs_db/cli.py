#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Command line interface for the Land Cover Classification System Database Model ."""
import click
from bdc_db.cli import cli
from bdc_db.db import db as _db
from flask.cli import with_appcontext

from lccs_db.data import load_dbdata


@cli.command()
@with_appcontext
@click.option('--ifile', type=click.File('r'),
              help='A SQL input file for insert.',
              required=False)
def insert_lccs_data(ifile):
    """Insert data in LCCS schema."""
    if ifile is not None:
        sql = ifile.read()
    else:
        sql = load_dbdata()

    _db.session.execute(sql)

    _db.session.commit()

    click.echo("LCCS Data inserted with success!")

def main(as_module=False):
    # TODO omit sys.argv once https://github.com/pallets/click/issues/536 is fixed
    import sys
    cli.main(args=sys.argv[1:], prog_name="python -m lccs_db" if as_module else None)