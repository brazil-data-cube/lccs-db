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

from sqlalchemy import (Column, ForeignKey, Index, Integer, LargeBinary,
                        PrimaryKeyConstraint, Text)
from sqlalchemy.orm import relationship

from ..config import Config
from .base import BaseModel


class Styles(BaseModel):
    """A Style class."""

    __tablename__ = 'styles'

    classification_system_id = Column(Integer, ForeignKey(f'{Config.LCCS_SCHEMA_NAME}.classification_systems.id',
                                                          onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    style_format_id = Column(Integer,
                             ForeignKey(f'{Config.LCCS_SCHEMA_NAME}.style_formats.id', onupdate='CASCADE',
                                        ondelete='CASCADE'), primary_key=True)
    style = Column(LargeBinary, nullable=False)
    mime_type = Column(Text, nullable=False, unique=False)
    classification_system = relationship('LucClassificationSystem', foreign_keys=[classification_system_id])
    style_format = relationship('StyleFormats', foreign_keys=[style_format_id])

    __table_args__ = (
        Index(None, classification_system_id),
        Index(None, style_format_id),
        Index(None, mime_type),
        PrimaryKeyConstraint('classification_system_id', 'style_format_id'),
        dict(schema=Config.LCCS_SCHEMA_NAME),
    )
