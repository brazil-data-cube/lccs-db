#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from sqlalchemy import Column, Index, Integer, Text, UniqueConstraint

from ..config import Config
from .base import BaseModel


class StyleFormats(BaseModel):
    """A StyleFormats class."""

    __tablename__ = 'style_formats'
    __table_args__ = dict(schema=Config.LCCS_SCHEMA_NAME)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)

    __table_args__ = (
        Index(None, name),
        UniqueConstraint(name),
        dict(schema=Config.LCCS_SCHEMA_NAME),
    )
