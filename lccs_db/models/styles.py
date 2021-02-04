#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from sqlalchemy import (JSON, Column, ForeignKey, Index, Integer, LargeBinary,
                        PrimaryKeyConstraint, Text)
from sqlalchemy.orm import relationship

from ..config import Config
from .base import BaseModel


class Styles(BaseModel):
    """A Style class."""

    __tablename__ = 'styles'

    class_system_id = Column(Integer, ForeignKey(f'{Config.LCC_ACTIVE_SCHEMA}.class_systems.id',
                                                 onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    style_format_id = Column(Integer,
                             ForeignKey(f'{Config.LCC_ACTIVE_SCHEMA}.style_formats.id', onupdate='CASCADE',
                                        ondelete='CASCADE'), primary_key=True)

    style = Column(LargeBinary, nullable=False)

    mime_type = Column(Text, nullable=False, unique=False)

    classification_system = relationship('LucClassificationSystem', foreign_keys=[class_system_id])
    style_format = relationship('StyleFormats', foreign_keys=[style_format_id])

    __table_args__ = (
        Index(None, class_system_id),
        Index(None, style_format_id),
        Index(None, mime_type),
        PrimaryKeyConstraint('class_system_id', 'style_format_id'),
        dict(schema=Config.LCC_ACTIVE_SCHEMA),
    )
