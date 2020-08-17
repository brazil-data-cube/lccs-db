#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Defines flask extension module for the Land Cover Classification System Database Model."""
from flask import Flask

from .cli import cli


class LCCSDatabase:
    def __init__(self, app=None, **kwargs):
        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app: Flask, **kwargs):
        app.extensions['lccs-db'] = self
        app.cli.add_command(cli)