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

from sqlalchemy import (Column, ForeignKey, Index, Integer, Numeric,
                        PrimaryKeyConstraint, Text)
from sqlalchemy.orm import relationship

from ..config import Config
from .base import BaseModel


class ClassMapping(BaseModel):
    """A class that represents Class Mapping"""

    __tablename__ = 'class_mappings'

    source_class_id = Column(Integer, ForeignKey(f'{Config.LCCS_SCHEMA_NAME}.classes.id', onupdate='CASCADE',
                                                 ondelete='CASCADE'), nullable=False)
    target_class_id = Column(Integer, ForeignKey(f'{Config.LCCS_SCHEMA_NAME}.classes.id', onupdate='CASCADE',
                                                 ondelete='CASCADE'), nullable=False)
    
    description = Column(Text, nullable=True)
    degree_of_similarity = Column(Numeric, nullable=True)

    source_class = relationship("LucClass", foreign_keys=[source_class_id])
    target_class = relationship("LucClass", foreign_keys=[target_class_id])

    __table_args__ = (
        Index(None, source_class_id),
        Index(None, target_class_id),
        PrimaryKeyConstraint('source_class_id', 'target_class_id'),
        dict(schema=Config.LCCS_SCHEMA_NAME),
    )