#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from .base import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from ..config import Config


class Style(BaseModel):
    """Style."""

    __tablename__ = 'style'
    __table_args__ = (
        PrimaryKeyConstraint('class_system_id', 'application_style_id'),
        {'schema': Config.ACTIVITIES_SCHEMA}
    )

    class_system_id = Column(Integer, ForeignKey('{}.class_systems.id'.format(Config.ACTIVITIES_SCHEMA),
                                                 ondelete='NO ACTION'), nullable=False, primary_key=True)
    application_style_id = Column(Integer, ForeignKey('{}.applications_style.id'.format(Config.ACTIVITIES_SCHEMA),
                                                      ondelete='NO ACTION'), nullable=False, primary_key=True)

    classification_system = relationship('LucClassificationSystem', foreign_keys=[class_system_id])
    application_style = relationship('ApplicationsStyle', foreign_keys=[application_style_id])
