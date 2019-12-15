#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Land Cover Classification System Model ."""

from sqlalchemy import Column, Integer, Text

from .base import BaseModel


class LucClassificationSystem(BaseModel):
    """LucClassificationSystem."""

    __tablename__ = 'classification_system'
    __table_args__ = {'schema': 'luc'}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    authority_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    version = Column(Text, nullable=False)