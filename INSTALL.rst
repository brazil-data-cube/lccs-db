..
    This file is part of Land Cover Classification System Database Model.
    Copyright (C) 2019 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Installation
============

``lccs-db`` depends essentially on `Flask-Alembic <https://bitbucket.org/davidism/flask-alembic/src/default/>`_. Please, read the instructions below in order to install ``lccs-db``.

Production Installation
-----------------------

Install from GitHub:

.. code-block:: shell

    pip3 install git+https://github.com/brazil-data-cube/lccs-db@b-0.2

Development Installation
------------------------

Clone the software repository:

.. code-block:: shell

    $ git clone https://github.com/brazil-data-cube/lccs-db.git


Go to the source code folder:

.. code-block:: shell

    $ cd lccs-db


Use pip to install in development mode:

.. code-block:: shell

    $ pip3 install -e .[all]


Run the tests:

.. code-block:: shell

    $ ./run-tests.sh


Generate the documentation:

.. code-block:: shell

    $ python setup.py build_sphinx


The above command will generate the documentation in HTML and it will place it under:

.. code-block:: shell

    doc/sphinx/_build/html/


.. note::

    If you want to create the database model, please, see `RUNNING.rst <./RUNNING.rst>`_.