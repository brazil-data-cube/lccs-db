#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
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
]

tests_require = [
    'coverage>=4.5',
    'coveralls>=1.8',
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

extras_require['all'] = [ req for exts, reqs in extras_require.items() for req in reqs ]

setup_requires = [
    'pytest-runner>=5.2',
]

install_requires = [
    'SQLAlchemy[postgresql_psycopg2binary]>=1.3.10',
    'alembic>=1.0.10',
    'Flask-Alembic>=2.0,<3',
    'Flask-SQLAlchemy>=2.4.1',
    'sqlalchemy-utils>=0.36.0'
    'Click>=7.0',
    'bdc-db @ git+git://github.com/brazil-data-cube/bdc-db.git#egg=bdc-db'
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
    keywords=['Land Use Land Cover', 'GIS', 'Database', 'Model', 'Classification System'],
    license='MIT',
    author='INPE',
    author_email='brazildatacube@dpi.inpe.br',
    url='https://github.com/brazil-data-cube/lccs-db',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'lccs_db = lccs_db.cli:cli',
        ],
        'bdc_db.alembic': [
            'lccs_db = lccs_db:alembic'
        ],
        'bdc_db.models': [
            'lccs_db = lccs_db.models'
        ]
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)