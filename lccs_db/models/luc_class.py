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
    """LucClassificationSystem."""

    __tablename__ = 'luc_class'
    __table_args__ = {'schema': 'bdc'}

    id = Column(Integer, primary_key=True)
    codigo = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    luc_classification_system_id = Column(Integer, ForeignKey('luc_classification_system.id',
                                                              ondelete='NO ACTION'), nullable=False)
    parent_id = Column(Integer, ForeignKey('luc_class.id', ondelete='NO ACTION'), nullable=True)

    luc_classification_system = relationship('LucClassificationSystem')