..
    This file is part of Land Cover Classification System Database Model.
    Copyright (C) 2019 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Installation
============

``lccs-db`` depends essentially on `Alembic <https://alembic.sqlalchemy.org/>`_. Please, read the instructions below in order to install ``lccs-db``.


Production installation
-----------------------

**Under Development!**

.. Install from `PyPI <https://pypi.org/>`_:
..
.. .. code-block:: shell
..
..     $ pip3 install lccs-db


Development installation
------------------------

Clone the software repository:

.. code-block:: shell

        $ git clone https://github.com/brazil-data-cube/lccs-db.git


Go to the source code folder:

.. code-block:: shell

        $ cd lccs-db


Install in development mode:

.. code-block:: shell

        $ pip3 install -e .[all]


Run the tests:

.. code-block:: shell

        $ ./run-test.sh


Generate the documentation:

.. code-block:: shell

        $ python setup.py build_sphinx


The above command will generate the documentation in HTML and it will place it under:

.. code-block:: shell

    doc/sphinx/_build/html/

**Note:** If you want to create the database model, please, see `RUNNING.rst <./RUNNING.rst>`_.