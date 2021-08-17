#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from sqlalchemy import Column, Index, Integer, String, UniqueConstraint

from ..config import Config
from .base import BaseModel


class StyleFormats(BaseModel):
    """A StyleFormats class."""

    __tablename__ = 'style_formats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    type_identifier = Column(String(255), nullable=True, comment='type for which to produce the style_format')

    __table_args__ = (
        Index(None, name),
        UniqueConstraint(name, type, type_identifier),
        dict(schema=Config.LCCS_SCHEMA_NAME),
    )
