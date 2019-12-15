#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from .base import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

class LucClass(BaseModel):
    """LucClass."""

    __tablename__ = 'class'
    __table_args__ = {'schema': 'luc'}

    id = Column(Integer, primary_key=True)
    code = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    style = Column(Text, nullable=False)
    classification_system_id = Column(Integer, ForeignKey('luc.classification_system.id',
                                                              ondelete='NO ACTION'), nullable=False)

    parent_id = Column(Integer, ForeignKey('luc.class.id', ondelete='NO ACTION'), nullable=True)

    classification_system = relationship('LucClassificationSystem')