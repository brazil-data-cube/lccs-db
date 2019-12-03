#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from .base import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, Text, Numeric
from sqlalchemy.orm import relationship

class ClassMapping(BaseModel):
    """ClassMapping."""

    __tablename__ = 'class_mapping'
    __table_args__ = {"schema": "bdc"}

    source_class_id = Column(Integer, ForeignKey('luc_class.id', ondelete='NO ACTION'), nullable=False, primary_key=True)
    target_class_id = Column(Integer, ForeignKey('luc_class.id', ondelete='NO ACTION'), nullable=False, primary_key=True)
    description = Column(Text, nullable=False)
    degree_of_similarity = Column(Numeric, nullable=False)

    source_class = relationship('LucClass', foreign_keys=[source_class_id])
    target_class = relationship('LucClass', foreign_keys=[target_class_id])