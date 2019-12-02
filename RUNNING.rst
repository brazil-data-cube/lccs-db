..
    This file is part of Land Cover Classification System Database Model.
    Copyright (C) 2019 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Running
=======

LCCS-DB utilizes `Alembic <https://alembic.sqlalchemy.org/>`_. For running the migration script you will need to create a database repository first.

In PostgreSQL this can be accomplished in the ``psql`` terminal with the following commands:

.. code-block:: sql

        CREATE DATABASE lccs_db TEMPLATE template1;

        \c lccs_db

        CREATE EXTENSION postgis;


After that, run migration command to prepare the LCCS data model:

.. code-block:: bash

        alembic upgrade head


**Note:** Before running the above command, make sure that the ``alembic.ini`` has a proper value set for the key ``sqlalchemy.url``.

If all the commands succeed, for PostgreSQL you can check the created table within the ``psql`` terminal as follow:

.. code-block:: sql

        \dt bdc.*


You should get a similar output::

                           List of relations
         Schema |           Name            | Type  |  Owner
        --------+---------------------------+-------+----------
         bdc    | class_mapping             | table | postgres
         bdc    | luc_class                 | table | postgres
         bdc    | luc_classification_system | table | postgres
        (3 rows)
