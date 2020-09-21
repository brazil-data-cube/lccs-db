#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model Exemple."""

from lccs_db.cli import create_app
from lccs_db.models import LucClassificationSystem

class_systems = [
    {
        "name": "PRODES",
        "authority_name": "INPE",
        "description": "Projeto de monitoramento ambiental anual. ",
        "version": "1.0"
    },
    {
        "name": "Deter-A",
        "authority_name": "INPE",
        "description": "Sistema de Alerta de Desmatamento",
        "version": "1.0"
    },
    {
        "name": "TerraClass_AMZ",
        "authority_name": "INPE",
        "description": "Mapeamento de uso e cobertura do solo de áreas mapeadas como desmatamento pelo PRODES",
        "version": "1.0"
    },
    {
        "name": "MapBiomas3.1",
        "authority_name": "Mapbiomas",
        "description": "Mapeamento de uso e cobertura do solo. Coleção 3",
        "version": "3.1"
    }
]

def verify_class_system_exist(class_system_name):

    try:
        class_system = LucClassificationSystem.get(name=class_system_name)
        return class_system
    except BaseException:
       return None

if __name__ == '__main__':
    # Initialize SQLAlchemy Models

    app = create_app()

    with app.app_context():

        for class_system in class_systems:

            class_system = verify_class_system_exist(class_system['name'])

            if class_system:
                print("Classification System {} already exist".format(class_system.name))
            else:
                class_system = LucClassificationSystem()
                class_system.authority_name = class_system['authority_name']
                class_system.description = class_system['description']
                class_system.name = class_system['name']
                class_system.version = class_system['version']
                class_system.save()

                print("Classification System {} inserted!".format(class_system.name))