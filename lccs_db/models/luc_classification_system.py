#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Land Cover Classification System Model ."""

from sqlalchemy import (Column, ForeignKey, Index, Integer,
                        PrimaryKeyConstraint, String, Text, Unicode,
                        UnicodeText, UniqueConstraint)

from ..config import Config
from .base import BaseModel


class LucClassificationSystem(BaseModel):
    """A LucClassificationSystem class represent a Classification System."""

    __tablename__ = 'classification_systems'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    authority_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    version = Column(String(3), nullable=False)
    version_predecessor = Column(ForeignKey(id, onupdate='CASCADE', ondelete='CASCADE'))
    version_successor = Column(ForeignKey(id, onupdate='CASCADE', ondelete='CASCADE'))

    __table_args__ = (
        UniqueConstraint(name, version),
        Index(None, name),
        dict(schema=Config.LCCS_SCHEMA_NAME)
    )


class ClassificationSystemSRC(BaseModel):
    """Model for Classification System provenance/lineage."""

    tablename = 'classification_system_src'

    classification_system_id = Column('classification_system_id', Integer,
                                      ForeignKey(LucClassificationSystem.id, onupdate='CASCADE', ondelete='CASCADE'),
                                      nullable=False)

    classification_system_src_id = Column('classification_system_src_id', Integer,
                                          ForeignKey(LucClassificationSystem.id, onupdate='CASCADE', ondelete='CASCADE'),
                                          nullable=False)

    table_args = (
        PrimaryKeyConstraint(classification_system_id, classification_system_src_id),
        dict(schema=Config.LCCS_SCHEMA_NAME),
    )
