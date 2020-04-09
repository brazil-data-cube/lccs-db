#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from sqlalchemy import JSON, Column, ForeignKey, Integer, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from ..config import Config
from .base import BaseModel


class Styles(BaseModel):
    """Style."""

    __tablename__ = 'styles'
    __table_args__ = (
        PrimaryKeyConstraint('class_system_id', 'style_format_id'),
        {'schema': Config.LCC_ACTIVE_SCHEMA}
    )

    class_system_id = Column(Integer, ForeignKey('{}.class_systems.id'.format(Config.LCC_ACTIVE_SCHEMA),
                                                 ondelete='NO ACTION'), nullable=False, primary_key=True)
    style_format_id = Column(Integer, ForeignKey('{}.style_formats.id'.format(Config.LCC_ACTIVE_SCHEMA),
                                                      ondelete='NO ACTION'), nullable=False, primary_key=True)

    style = Column(JSON, nullable=True)

    classification_system = relationship('LucClassificationSystem', foreign_keys=[class_system_id])
    style_format = relationship('StyleFormats', foreign_keys=[style_format_id])
