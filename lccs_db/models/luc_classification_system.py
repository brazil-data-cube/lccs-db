#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Land Cover Classification System Model ."""

from sqlalchemy import Column, Integer, Text

from ..config import Config
from .base import BaseModel


class LucClassificationSystem(BaseModel):
    """A LucClassificationSystem class represent a Classification System."""

    __tablename__ = 'class_systems'
    __table_args__ = dict(schema=Config.LCC_ACTIVE_SCHEMA)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    authority_name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    version = Column(Text, nullable=True)