..
    This file is part of Land Cover Classification System Database Model.
    Copyright (C) 2019-2022 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


.. _Installation:

Installation
============


Pre-Requirements
----------------


``lccs-db`` depends essentially on:

- `BDC-DB <https://github.com/brazil-data-cube/bdc-db>`_: a database management extension for Brazil Data Cube Applications and Services.

- `Flask-SQLAlchemy <https://flask-sqlalchemy.palletsprojects.com/en/2.x/>`_: an extension for `Flask <http://flask.pocoo.org/>`_ that adds support for `SQLAlchemy <https://www.sqlalchemy.org/>`_ in applications.

- `Flask-Alembic <https://flask-alembic.readthedocs.io/en/stable//>`_: used to handle `SQLAlchemy <https://www.sqlalchemy.org/>`_ database migrations with `Alembic <https://alembic.sqlalchemy.org/en/latest/index.html>`_.

- `SQLAlchemy-Utils <https://sqlalchemy-utils.readthedocs.io/en/latest/index.html>`_: utility functions for SQLAlchemy such as database creation, database existence test, SQL script running.


Development Installation - GitHub
---------------------------------


Clone the Software Repository
+++++++++++++++++++++++++++++


Use ``git`` to clone the software repository::

    git clone https://github.com/brazil-data-cube/lccs-db.git


Install LCCS-DB in Development Mode
+++++++++++++++++++++++++++++++++++


Go to the source code folder::

    cd lccs-db


Install in development mode::

    pip3 install -e .[all]


.. note::

    If you want to create a new *Python Virtual Environment*, please, follow this instruction:

    *1.* Create a new virtual environment linked to Python 3.7::

        python3.7 -m venv venv


    **2.** Activate the new environment::

        source venv/bin/activate


    **3.** Update pip and setuptools::

        pip3 install --upgrade pip

        pip3 install --upgrade setuptools


Run the Tests
+++++++++++++


.. code-block:: shell

    export SQLALCHEMY_DATABASE_URI="postgresql://postgres:secret@localhost:5432/bdc_db"

    ./run-tests.sh


Build the Documentation
+++++++++++++++++++++++


You can generate the documentation based on Sphinx with the following command::

    python setup.py build_sphinx


The above command will generate the documentation in HTML and it will place it under::

    docs/sphinx/_build/html/


You can open the above documentation in your favorite browser, as::

    firefox docs/sphinx/_build/html/index.html


Production Installation - GitHub
--------------------------------


Install from GitHub::

    pip3 install git+https://github.com/brazil-data-cube/lccs-db@v0.8.0
