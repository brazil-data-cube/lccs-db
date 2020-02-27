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
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

class ParentClasses(BaseModel):
    """LucClass."""

    __tablename__ = 'parent_classes'
    __table_args__ = dict(schema=Config.ACTIVITIES_SCHEMA)

    class_parent_id = Column(Integer, ForeignKey('{}.classes.id'.format(Config.ACTIVITIES_SCHEMA), ondelete='NO ACTION'), nullable=True)
    class_id = Column(Integer, ForeignKey('{}.classes.id'.format(Config.ACTIVITIES_SCHEMA), ondelete='NO ACTION'), nullable=True, primary_key=True)

    class_parent = relationship('classes_parent')
    classe = relationship('classes_parent')