#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from sqlalchemy import (Column, ForeignKey, Index, Integer, Text,
                        UniqueConstraint, select)
from sqlalchemy.orm import aliased, relationship
from sqlalchemy_utils import create_view

from ..config import Config
from .base import BaseModel
from .luc_classification_system import LucClassificationSystem


class LucClass(BaseModel):
    """A LucClass class represent a Class of an Classification System."""

    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(Text, nullable=False)
    name = Column(Text, nullable=False)

    description = Column(Text, nullable=False)

    class_system_id = Column(Integer, ForeignKey(f'{Config.LCCS_SCHEMA_NAME}.class_systems.id',
                                                 onupdate='CASCADE', ondelete='CASCADE'))

    class_parent_id = Column(Integer, ForeignKey(f'{Config.LCCS_SCHEMA_NAME}.classes.id', onupdate='CASCADE',
                                                 ondelete='CASCADE'))

    classification_system = relationship('LucClassificationSystem')

    class_parent = relationship('LucClass')

    __table_args__ = (
        Index(None, name),
        Index(None, code),
        Index(None, class_system_id),
        UniqueConstraint(name, class_system_id),
        dict(schema=Config.LCCS_SCHEMA_NAME),
    )


class ClassesView(BaseModel):
    """A LucClass View."""
    __tablename__ = 'v_classes'
    parent_classes = aliased(LucClass)

    __table__ = create_view(
        name=__tablename__,
        selectable=select(
            [LucClass.created_at,
             LucClass.updated_at,
             LucClass.id,
             LucClass.name,
             LucClass.description,
             LucClass.code,
             parent_classes.name.label('class_parent_name'),
             LucClassificationSystem.name.label('class_system_name')],
            from_obj=(
                LucClass.__table__.join(LucClassificationSystem, LucClassificationSystem.id == LucClass.class_system_id)
                    .join(parent_classes, LucClass.class_parent_id == parent_classes.id, isouter=True))
        ),
        metadata=BaseModel.metadata,
    )
    __table__.schema = Config.LCCS_SCHEMA_NAME
