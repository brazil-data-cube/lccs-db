..
    This file is part of Land Cover Classification System Database Model.
    Copyright (C) 2019-2020 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


===============================================
Land Cover Classification System Database Model
===============================================

.. image:: https://img.shields.io/badge/license-MIT-green
        :target: https://github.com//brazil-data-cube/lccs-db/blob/master/LICENSE
        :alt: Software License


.. image:: https://travis-ci.org/brazil-data-cube/lccs-db.svg?branch=master
        :target: https://travis-ci.org/brazil-data-cube/lccs-db
        :alt: Build Status


.. image:: https://coveralls.io/repos/github/brazil-data-cube/lccs-db/badge.svg?branch=master
        :target: https://coveralls.io/github/brazil-data-cube/lccs-db?branch=master
        :alt: Code Coverage Test


.. image:: https://readthedocs.org/projects/lccs-db/badge/?version=master
        :target: https://lccs-db.readthedocs.io/en/master/
        :alt: Documentation Status


.. image:: https://img.shields.io/badge/lifecycle-experimental-orange.svg
        :target: https://www.tidyverse.org/lifecycle/#experimental
        :alt: Software Life Cycle


.. image:: https://img.shields.io/github/tag/brazil-data-cube/lccs-db.svg
        :target: https://github.com/brazil-data-cube/lccs-db/releases
        :alt: Release


.. image:: https://img.shields.io/discord/689541907621085198?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/689541907621085198#
        :alt: Join us at Discord


.. role:: raw-html(raw)
    :format: html


O que é o LCCS-DB?
==================


Atualmente existem diversos conjuntos de dados em escalas regionais, nacionais e globais com informação sobre uso e cobertura da terra que visam atender a um grande número de aplicações, entre elas a gestão de recursos naturais, mudanças do clima e seus impactos e conservação da biodiversidade. Esses produtos de dados são gerados utilizando diferentes abordagens e metodologias, que apresentam informações sobre diferentes classes da superfície da terra, como florestas, plantações agrícolas, entre outras. As iniciativas que geram mapas de uso e cobertura da terra, normalmente desenvolvem seu próprio sistema de classificação, com diferentes nomenclaturas e significados das classes utilizadas.


:raw-html:`<br />`
Neste contexto, o **LCCS-DB** (**L**\ and **C**\ over **C**\ lassification **S**\ystem **D**\ ata\ **b**\ ase) fornece um modelo de dados que representa os diversos sistemas de classificação em uso e suas respectivas classes. O LCCS-DB tem por objetivo disponibilizar um repositório de dados para facilitar o acesso e visualização das classes e suas simbologias em cada sistema de classificação empregados nos projetos que disponibilizam mapas de uso e cobertura da terra no Brasil: `PRODES <http://www.obt.inpe.br/OBT/assuntos/programas/amazonia/prodes>`_, `DETER <http://www.obt.inpe.br/OBT/assuntos/programas/amazonia/deter>`_, `TerraClass <http://www.inpe.br/cra/projetos_pesquisas/dados_terraclass.php>`_ e MapBiomas.


:raw-html:`<br />`
Além disso, o LCCS-DB permite realizar o mapeamento entre as classes dos sistemas de classificação de maneira a simplificar análise conjunta dos dados.


:raw-html:`<br />`
O diagrama ER abaixo apresenta as tabelas utilizadas neste sistema:

.. image:: https://github.com/brazil-data-cube/lccs-db/raw/master/doc/spec/lccs_database.png
        :target: https://github.com/brazil-data-cube/lccs-db/tree/master/doc/spec
        :width: 90%
        :alt: Database Schema


:raw-html:`<br />`
Este pacote é a base para os seguintes projetos:

- `LCCS-WS <https://github.com/brazil-data-cube/lccs-ws>`_: Land Cover Classification System Web Service (see also `its specification <https://github.com/brazil-data-cube/lccs-ws-spec>`_).

- `LCCS.py <https://github.com/brazil-data-cube/lccs.py>`_: Python Client Library for Land Cover Classification System Web Service.

- `WLTS <https://github.com/brazil-data-cube/lccs.py>`_: Web Land Trajectory Service.


Installation
============


Install from GitHub::

    pip3 install git+https://github.com/brazil-data-cube/lccs-db@b-0.4


Documentation
=============


See https://lccs-db.readthedocs.io/en/latest/


License
=======


.. admonition::
    Copyright (C) 2019-2020 INPE.

    Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

