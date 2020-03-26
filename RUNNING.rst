..
    This file is part of Land Cover Classification System Database Model.
    Copyright (C) 2019 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Running LCCS-DB in the Command Line
===================================

Create a PostgreSQL database and ``lccs`` schema if not exist.

.. code-block:: shell

        SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
        lccs_db db init-db


After that, run Flask-Alembic command command to prepare the LCCS-DB data model:

.. code-block:: shell

        SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
        lccs_db alembic upgrade head

If all the commands succeed, for PostgreSQL you can check the created table within the ``psql`` terminal as follow:

.. code-block:: sql

        \dt lccs.*


You should get a similar output::

                           List of relations
         Schema  |           Name            | Type  |  Owner
        ---------+---------------------------+-------+----------
         lccs    | applications_style        | table | postgres
         lccs    | class_mapping             | table | postgres
         lccs    | class                     | table | postgres
         lccs    | classification_system     | table | postgres
         lccs    | parent_classes            | table | postgres
         lccs    | style                     | table | postgres
        (3 rows)

Updating an Existing Data Model
===============================

In order to make changes to the models of a module, we need to create a new alembic revision.
To make sure that database is up to date, use the following:

.. code-block:: shell

        SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
        lccs_db alembic upgrade heads

Updating the Migration Scripts
==============================

.. code-block:: shell

        SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
        lccs_db alembic revision "Revision message"


Adding lccs_db as dependency to existing modules
================================================

The following steps assume that sample_db is the name of the module for which you are adding alembic support.

The module lccs_db uses dynamic model loading in order to track both lccs_db and others python modules. It was built on top of ``Python Setup entry_points``.

In order to load models dynamically, you must edit ``setup.py`` in your package sample_db and append your module alembic and models to the following entry points:

- **sample_db.alembic** defines where migrations will be stored.
- **sample_db.models** defines where SQLAlchemy models will be mapped.

The ``setup.py`` should be like as follows:

.. code-block:: python

        setup(
           ...,
            entry_points={
            'lccs_db.alembic': [
                'sample_db = sample_db:alembic'
            ],
            'lccs_db.models': [
                'sample_db = sample_db.models'
            ]
          },
        )

This will register the ``sample_db/alembic`` directory in the alembic's version locations. It also will make the ``sample_db/models`` be discoverable and loaded in memory to track alembic revisions.

Creating a new revision
-----------------------

To create a new revision for module ``sample_db``, you must create a branch and get latest revision id to make persistent migration. Use the following command to get latest revision id:

.. code-block:: shell

        SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
        lccs_db alembic heads

The result will be something like that:

.. code-block:: shell

        <base> -> 7661f3f76beb (default) (head), create-initial-tables

In this example, the latest ``revision id`` is ``7661f3f76beb``.

In order to do generate migration for your module, use the following command:

.. code-block:: shell

        SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
        lccs_db alembic revision "Revision message." \
            --path your_module_name/alembic \
            --branch your_module_name \
            --parent 7661f3f76beb

**Note**:

The ``--parent`` argument is required only in the first revision generation. When a parent is not given for other modules the revision will be placed into ``default branch ()`` and you may face issues during ``lccs_db alembic upgrade``.