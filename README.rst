..
    This file is part of Land Cover Classification System Database Model.
    Copyright (C) 2019-2022 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


===============================================
Land Cover Classification System Database Model
===============================================


.. image:: https://img.shields.io/badge/license-MIT-green
        :target: https://github.com//brazil-data-cube/lccs-db/blob/master/LICENSE
        :alt: Software License


.. image:: https://drone.dpi.inpe.br/api/badges/brazil-data-cube/lccs-db/status.svg
        :target: https://drone.dpi.inpe.br/brazil-data-cube/lccs-db
        :alt: Build Status


.. image:: https://codecov.io/gh/brazil-data-cube/lccs-db/branch/master/graph/badge.svg?token=C10H8AAV2A
        :target: https://codecov.io/gh/brazil-data-cube/lccs-db
        :alt: Code Coverage Test


.. image:: https://readthedocs.org/projects/lccs-db/badge/?version=latest
        :target: https://lccs-db.readthedocs.io/en/latest/
        :alt: Documentation Status


.. image:: https://img.shields.io/badge/lifecycle-maturing-blue.svg
        :target: https://www.tidyverse.org/lifecycle/#maturing
        :alt: Software Life Cycle


.. image:: https://img.shields.io/github/tag/brazil-data-cube/lccs-db.svg
        :target: https://github.com/brazil-data-cube/lccs-db/releases
        :alt: Release


.. image:: https://img.shields.io/discord/689541907621085198?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/689541907621085198#
        :alt: Join us at Discord


.. role:: raw-html(raw)
    :format: html


About
=====


Currently, there are several data sets on regional, national and global scales with information on land use and land cover that aim to support a large number of applications, including the management of natural resources, climate change and its impacts, and biodiversity conservation. These data products are generated using different approaches and methodologies, which present information about different classes of the earth's surface, such as forests, agricultural plantations, among others. Initiatives that generate land use and land cover maps normally develop their own classification system, with different nomenclatures and meanings of the classes used.


**LCCS-DB** (**L**\ and **C**\ over **C**\ lassification **S**\ystem **D**\ ata\ **b**\ ase) provides a data model that represents the various classification systems in use and their respective classes. The LCCS-DB aims to provide a data repository to facilitate access and visualization of classes and their symbologies in each classification system employed in projects that provide land use and land cover maps in Brazil: `PRODES <http://www.obt.inpe.br/OBT/assuntos/programas/amazonia/prodes>`_, `DETER <http://www.obt.inpe.br/OBT/assuntos/programas/amazonia/deter>`_, `TerraClass <http://www.inpe.br/cra/projetos_pesquisas/dados_terraclass.php>`_ and MapBiomas.


In addition, the LCCS-DB allows mapping between classes of classification systems in order to simplify joint data analysis.


The following diagram shows the tables used in this system:


.. image:: https://github.com/brazil-data-cube/lccs-db/raw/master/docs/spec/lccs_database.png
        :target: https://github.com/brazil-data-cube/lccs-db/tree/master/docs/spec
        :width: 90%
        :alt: Database Schema


:raw-html:`<br />`
This is the base package for other softwares in the Brazil Data Cube project:

- `LCCS-WS-SPEC <https://github.com/brazil-data-cube/lccs-ws-spec>`_: Land Cover Classification System Web Service specification.

- `LCCS-WS <https://github.com/brazil-data-cube/lccs-ws>`_: Land Cover Classification System Web Service implementation.

- `LCCS.py <https://github.com/brazil-data-cube/lccs.py>`_: Python Client Library for Land Cover Classification System Web Service.

- `WLTS-SPEC <https://github.com/brazil-data-cube/wlts-spec>`_: Web Land Trajectory Service Specification.

- `WLTS.py <https://github.com/brazil-data-cube/wlts.py>`_: Python Client Library for Web Land Trajectory Service.

- `BDC-Catalog <https://github.com/brazil-data-cube/bdc-catalog>`_: Brazil Data Cube Image Metadata Catalog.


Installation
============


Install from GitHub::

    pip3 install git+https://github.com/brazil-data-cube/lccs-db@v0.8.0


Documentation
=============


See https://lccs-db.readthedocs.io/en/latest/


License
=======


.. admonition::
    Copyright (C) 2019-2022 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

