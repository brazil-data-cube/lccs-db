#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model Exemple."""

import os
import sys
from flask import Flask

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('../'))

from lccs_db.models import db, LucClassificationSystem
from lccs_db.cli import create_app

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

if __name__ == '__main__':
    # Initialize SQLAlchemy Models


    _app = create_app()

    with _app.app_context():

        for class_system in class_systems:
            try:
                luc_system = LucClassificationSystem.get(name=class_system['name'])
            except BaseException:
                luc_system = LucClassificationSystem()
                luc_system.authority_name = class_system['authority_name']
                luc_system.description = class_system['description']
                luc_system.name = class_system['name']
                luc_system.version = class_system['version']
                luc_system.save()

    print("Finish!")