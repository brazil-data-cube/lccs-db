#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from .base import BaseModel
from ..config import Config

from sqlalchemy import Column, ForeignKey, Integer, Text, Numeric, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

class ClassMapping(BaseModel):
    """ClassMapping."""

    __tablename__ = 'class_mappings'
    __table_args__ = (
        PrimaryKeyConstraint('source_class_id', 'target_class_id'),
        {'schema':Config.ACTIVITIES_SCHEMA}
    )

    source_class_id = Column(Integer, ForeignKey('{}.classes.id'.format(Config.ACTIVITIES_SCHEMA), ondelete='NO ACTION'), nullable=False)
    target_class_id = Column(Integer, ForeignKey('{}.classes.id'.format(Config.ACTIVITIES_SCHEMA), ondelete='NO ACTION'), nullable=False)
    description = Column(Text, nullable=True)
    degree_of_similarity = Column(Numeric, nullable=True)

    source_class = relationship("LucClass")
    target_class = relationship("LucClass")