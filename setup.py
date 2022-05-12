#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2022 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Python for the Land Cover Classification System Database Model."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

history = open('CHANGES.rst').read()

docs_require = [
    'Sphinx>=2.2',
    'sphinx_rtd_theme',
    'sphinx-copybutton',
]

tests_require = [
    'coverage>=4.5',
    'pytest>=5.2',
    'pytest-cov>=2.8',
    'pytest-pep8>=1.0',
    'pydocstyle>=4.0',
    'isort>4.3',
    'sqlalchemy-diff>=0.1.3',
    'alembic-verify>=0.1.4',
    'check-manifest>=0.40'
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
}

extras_require['all'] = [req for _, reqs in extras_require.items() for req in reqs]

setup_requires = [
    'pytest-runner>=5.2',
]

install_requires = [
    'Flask>=1.1.0',
    'Flask-SQLAlchemy>=2.4.0',
    'Flask-Alembic>=2.0.0',
    'bdc-db @ git+https://github.com/brazil-data-cube/bdc-db@v0.6.2'
]

packages = find_packages()

g = {}
with open(os.path.join('lccs_db', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='lccs_db',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    long_description_content_type = 'text/x-rst',
    keywords=['Land Use Land Cover', 'GIS', 'Database', 'Model', 'Classification System'],
    license='MIT',
    author='Brazil Data Cube Team',
    author_email='brazildatacube@inpe.br',
    url='https://github.com/brazil-data-cube/lccs-db',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'lccs-db = lccs_db.cli:cli',
        ],
        'bdc_db.alembic': [
            'lccs_db = lccs_db:alembic'
        ],
        'bdc_db.models': [
            'lccs_db = lccs_db.models'
        ],
        'bdc_db.scripts': [
            'lccs_db = lccs_db.scripts'
        ],
        'bdc_db.namespaces': [
            'lccs_db = lccs_db.config:Config.LCCS_SCHEMA_NAME'
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)
