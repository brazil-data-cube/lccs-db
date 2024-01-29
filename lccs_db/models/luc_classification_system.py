#
# This file is part of LCCS-DB.
# Copyright (C) 2022 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#
"""Land Cover Classification System Model ."""

from sqlalchemy import (Column, ForeignKey, Index, Integer,
                        PrimaryKeyConstraint, String, UniqueConstraint)
from sqlalchemy.dialects.postgresql import HSTORE
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.mutable import MutableDict

from ..config import Config
from .base import BaseModel, translation_hybrid


class LucClassificationSystem(BaseModel):
    """A LucClassificationSystem class represent a Classification System."""

    __tablename__ = 'classification_systems'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, comment='Classification System name internally.')
    title_translations = Column(MutableDict.as_mutable(HSTORE),
                                comment='A human-readable string naming for classification system.')
    title = translation_hybrid(title_translations)
    description_translations = Column(MutableDict.as_mutable(HSTORE))
    description = translation_hybrid(description_translations)
    authority_name = Column(String(255), nullable=False)
    version = Column(String(3), nullable=False)
    version_predecessor = Column(ForeignKey(id, onupdate='CASCADE', ondelete='CASCADE'))
    version_successor = Column(ForeignKey(id, onupdate='CASCADE', ondelete='CASCADE'))

    __table_args__ = (
        UniqueConstraint(name, version),
        Index(None, name),
        Index(None, title_translations),
        Index(None, description_translations),
        dict(schema=Config.LCCS_SCHEMA_NAME)
    )

    @hybrid_property
    def identifier(self):
        return self.name + '-' + self.version


class ClassificationSystemSRC(BaseModel):
    """Model for Classification System provenance/lineage."""

    __tablename__ = 'classification_system_src'

    classification_system_id = Column('classification_system_id', Integer,
                                      ForeignKey(LucClassificationSystem.id, onupdate='CASCADE', ondelete='CASCADE'),
                                      nullable=False)

    classification_system_src_id = Column('classification_system_src_id', Integer,
                                          ForeignKey(LucClassificationSystem.id, onupdate='CASCADE', ondelete='CASCADE'),
                                          nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(classification_system_id, classification_system_src_id),
        dict(schema=Config.LCCS_SCHEMA_NAME),
    )
