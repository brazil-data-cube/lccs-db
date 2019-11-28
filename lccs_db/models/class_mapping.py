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
    """LucClassificationSystem."""

    __tablename__ = 'class_mapping'
    __table_args__ = {'schema': 'bdc'}

    id = Column(Integer, primary_key=True)
    source_classification_sys_id = Column(Integer, ForeignKey('luc_classification_system.id', ondelete='NO ACTION'),
                                          nullable=False)
    target_classification_sys_id = Column(Integer,ForeignKey('luc_classification_system.id', ondelete='NO ACTION'),
                                          nullable=False)
    source_class_id = Column(Integer, ForeignKey('luc_class.id', ondelete='NO ACTION'), nullable=False)
    target_class_id = Column(Integer, ForeignKey('luc_class.id', ondelete='NO ACTION'), nullable=False)
    description = Column(Text, nullable=False)
    degree_of_similarity = Column(Numeric, nullable=False)

    source_classification_sys = relationship('LucClassificationSystem', foreign_keys=[source_classification_sys_id])
    target_classification_sys = relationship('LucClassificationSystem', foreign_keys=[target_classification_sys_id])
    source_class = relationship('LucClass', foreign_keys=[source_class_id])
    target_class = relationship('LucClass', foreign_keys=[target_class_id])