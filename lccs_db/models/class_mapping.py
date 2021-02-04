#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
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

    source_class_id = Column(Integer, ForeignKey(f'{Config.LCC_ACTIVE_SCHEMA}.classes.id', onupdate='CASCADE',
                                                 ondelete='CASCADE'))
    target_class_id = Column(Integer, ForeignKey(f'{Config.LCC_ACTIVE_SCHEMA}.classes.id', onupdate='CASCADE',
                                                 ondelete='CASCADE'))
    description = Column(Text, nullable=True)
    degree_of_similarity = Column(Numeric, nullable=True)

    source_class = relationship("LucClass", foreign_keys=[source_class_id])
    target_class = relationship("LucClass", foreign_keys=[target_class_id])

    __table_args__ = (
        Index(None, source_class_id),
        Index(None, target_class_id),
        PrimaryKeyConstraint('source_class_id', 'target_class_id'),
        dict(schema=Config.LCC_ACTIVE_SCHEMA),
    )