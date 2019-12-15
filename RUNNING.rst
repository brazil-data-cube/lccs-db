..
    This file is part of Land Cover Classification System Database Model.
    Copyright (C) 2019 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Running LCCS-DB in the Command Line
===================================

Create a PostgreSQL database:

.. code-block:: shell

        lccs_db --user postgres --host localhost --port 5432 --db_name sampledb init-db


After that, run migration command to prepare the LCCS data model:

.. code-block:: shell

        lccs_db --user postgres --host localhost --port 5442 --db_name sampledb init-alembic

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

Insert defaut data into data base:

.. code-block:: shell

        lccs_db --user postgres --host localhost --port 5442 --db_name sampledb insert-db

or:

.. code-block:: shell

        lccs_db --user postgres --host localhost --port 5442 --db_name sampledb insert-db --ifile insert.sql
