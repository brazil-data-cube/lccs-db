#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2021 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model Example."""

from lccs_db.models import LucClassificationSystem
from flask import Flask
from lccs_db.ext import LCCSDatabase
from lccs_db.models import db as _db
from lccs_db.models.base import translation_hybrid


system_inter = {
    "name": "uct",
    "title_translations": {'en': 'Land Use and Cover', 'pt-br': 'Uso e Cobertura da terra'},
    "authority_name": "LULC",
    "description_translations": {'en': 'Land use and land cover mapping.',
                                 'pt-br': 'Mapeamento de uso e cobertura do solo.'
                                 },
    "version": "1"
}


def verify_class_system_exist(class_system_name, version):
    try:
        classification_system = LucClassificationSystem.get(name=class_system_name, version=version)
        return classification_system
    except BaseException:
        return None


if __name__ == '__main__':
    # Initialize SQLAlchemy
    app = Flask(__name__)
    LCCSDatabase(app)

    with app.app_context():
        translation_hybrid.current_locale = 'pt-br'

        class_system = LucClassificationSystem()
        class_system.name = system_inter['name']
        class_system.title_translations = system_inter['title_translations']
        class_system.description_translations = system_inter['description_translations']
        class_system.authority_name = system_inter['authority_name']
        class_system.version = system_inter['version']
        class_system.save()

        print("Classification System {} inserted!".format(class_system.name))

        a = _db.session.query(LucClassificationSystem).first()

        print(a.name)
        print(a.title)
        print(a.identifier)
