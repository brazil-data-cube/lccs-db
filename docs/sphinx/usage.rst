..
    This file is part of Land Cover Classification System Database Model.
    Copyright (C) 2019-2020 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Usage
=====


Running LCCS-DB in the Command Line
-----------------------------------


If you have not installed ``lccs-db`` yet, please, take a look at the :ref:`Installation Guide <Installation>`.


Creating a PostgreSQL Database
++++++++++++++++++++++++++++++


If you do not have a database instance, you can create one with the command line utility ``lccs_db``::

    SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
    lccs_db db init


Create a schema (or namespace) named "``lccs``" in this database::

    SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
    lccs_db db create-namespaces


You can see all namespaces::

    SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
    lccs_db db show-namespaces


Creating the LCCS Data Model
++++++++++++++++++++++++++++


The command line utility ``lccs_db`` can also be used to create all tables belonging to the LCCS data model. The following command can be used to create or upgrade the table schema for LCCS::

    SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
    lccs_db alembic upgrade


If the above command succeed, you can check the created tables within the ``lccs`` schema in PostgreSQL. Use the ``psql`` terminal as follow::

    psql -U username -h host -p 5432 -d dbname -c "\dt lccs.*"


You should get a similar output::

                  List of relations
     Schema |      Name      | Type  |  Owner
    --------+----------------+-------+----------
     lccs   | class_mappings | table | postgres
     lccs   | class_systems  | table | postgres
     lccs   | classes        | table | postgres
     lccs   | style_formats  | table | postgres
     lccs   | styles         | table | postgres
    (5 rows)



Loading Default Class Systems
+++++++++++++++++++++++++++++


You can load well-known classification systems with the CLI::

    SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
    lccs_db db load-scripts


Loading Custom Class Systems
++++++++++++++++++++++++++++


You can load your own classification systems with the CLI::

    SQLALCHEMY_DATABASE_URI="postgresql://username:password@host:5432/dbname" \
    lccs_db db load-file --file "sql_file.sql"



.. note::

    For more information on ``lccs_db`` commands, please, type in the command line::

        lccs_db  --help
