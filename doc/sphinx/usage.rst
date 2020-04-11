..
    This file is part of Land Cover Classification System Database Model.
    Copyright (C) 2019 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Usage
=====


Setuptools Integration
----------------------

In order for the ``LCCS-DB CLI`` command to be aware of your models and upgrade recipies, you must specify the entry point in ``lccs_db.models`` group. ``LCCS-DB`` then takes care of loading the models automatically. Alembic configuration of version locations is assembled from ``lccs_db.alembic`` entry point group and is also managed by LCCC-DB. This mechanism relies on ``Python Setup entry_points``.


This section describes how to add ``LCCS-DB`` as dependency to an existing module. The steps assume that ``sample_db`` is the name of the module for which you are adding ``model classes`` and ``alembic`` support.


In order to load models dynamically, you must edit ``setup.py`` in your package ``sample_db`` and append your module ``alembic`` and ``models`` to the following entry points:

- ``sample_db.alembic``: defines where migrations will be stored.

- ``sample_db.models``: defines where SQLAlchemy models will be mapped.


The ``setup.py`` should contain an ``entry_points`` section as follows:

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
