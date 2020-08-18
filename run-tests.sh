#!/usr/bin/env bash
#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle --match-dir="^lccs_db/alembic" lccs_db setup.py && \
check-manifest --ignore ".travis-*" --ignore ".readthedocs.*" && \
pytest &&
sphinx-build -qnW --color -b doctest doc/sphinx/ doc/sphinx/_build/doctest