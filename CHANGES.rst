..
    This file is part of Land Cover Classification System.
    Copyright (C) 2019-2020 INPE.

    Land Cover Classification System is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Changes
=======

Version 0.8.1 (2022-07-20)
--------------------------

- Upgrade bdc-db to 0.6.2 (`#115 <https://github.com/brazil-data-cube/lccs-db/issues/115>`_).
- Add Babel dependency.


Version 0.8.0 (2022-02-07)
--------------------------

- Add table for transitions (`#81 <https://github.com/brazil-data-cube/lccs-db/issues/81>`_).
- Rename table `class_systems` to `classification_systems` (`#80 <https://github.com/brazil-data-cube/lccs-db/issues/80>`_).
- Add class system versioning (`#79 <https://github.com/brazil-data-cube/lccs-db/issues/79>`_).
- Add support I18N (`#78 <https://github.com/brazil-data-cube/lccs-db/issues/78>`_).
- Add custom decorator to assign language support (`#109 <https://github.com/brazil-data-cube/lccs-db/issues/109>`_).


Version 0.6.0 (2021-04-09)
--------------------------

- Add unique value in class (`#97 <https://github.com/brazil-data-cube/lccs-db/issues/97>`_).
- Review mandatory fields in the data model (`#89 <https://github.com/brazil-data-cube/lccs-db/issues/89>`_).
- Review table styles (`#87 <https://github.com/brazil-data-cube/lccs-db/issues/87>`_).
- Add symbology encoding for well known classification systems (`#86 <https://github.com/brazil-data-cube/lccs-db/issues/86>`_).
- Update Docker image used in tests  (`#91 <https://github.com/brazil-data-cube/lccs-db/issues/91>`_).
- Improve Unittest (`#83 <https://github.com/brazil-data-cube/lccs-db/issues/83>`_).
- Add UniqueConstraint in classification system (`#75 <https://github.com/brazil-data-cube/lccs-db/issues/75>`_).
- Add index in table (`#74 <https://github.com/brazil-data-cube/lccs-db/issues/74>`_).
- Add drone integration (`#71 <https://github.com/brazil-data-cube/lccs-db/issues/71>`_).


Version 0.4.1 (2021-03-17)
--------------------------

- Upgrade BDC-DB dependency to 0.4.3 to keep SQLAlchemy in version 1.3 until SQLAlchemyUtils is updated for SQLAlchemy 1.4. (`#99 <https://github.com/brazil-data-cube/lccs-db/issues/99>`_).


Version 0.4.0 (2020-12-09)
--------------------------

- Improved documentation.

- Compatibility with `BDC-DB Version 0.4.2 <https://github.com/brazil-data-cube/bdc-db>`_.

- Improved Sphinx template.


Version 0.2.0 (2020-04-11)
--------------------------

- First experimental version.

- Support for: Class Systems, Classes, Styles and Class Mappings.

- Command Line Interface support.

- ER diagram based on Draw.io.

- Documentation system based on Sphinx.

- Documentation integrated to ``Read the Docs``.

- Package support through Setuptools.

- Installation and use instructions.

- Database schema based on Flask-Alembic.

- Support for dynamic loading of model classes derived from LCCS-DB.

- Source code versioning based on `Semantic Versioning 2.0.0 <https://semver.org/>`_.

- License: `MIT <https://raw.githubusercontent.com/brazil-data-cube/lccs-db/v0.2.0/LICENSE>`_.