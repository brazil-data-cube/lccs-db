#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019-2020 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Model Configuration."""

from datetime import datetime

from bdc_db.db import db
from sqlalchemy import Column, DateTime

from ..config import Config

db.metadata.schema = Config.LCC_ACTIVE_SCHEMA


class BaseModel(db.Model):
    """Abstract class for ORM models."""
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(),
                        onupdate=datetime.utcnow())

    def save(self, commit=True):
        """Save and persists object in database."""
        db.session.add(self)

        if not commit:
            return

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self):
        """Delete object from database."""
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @classmethod
    def _filter(cls, **properties):
        """Filter abstraction."""
        return db.session.query(cls).filter_by(**properties)

    @classmethod
    def filter(cls, **properties):
        """Filter data set rows following the provided restrictions.

        Provides a wrapper of SQLAlchemy session query.

        :param properties: List of properties to filter of.
        :type properties: dict.
        """
        return cls._filter(**properties).all()

    @classmethod
    def get(cls, **restrictions):
        """Get one data set from database.

        Throws exception **NoResultFound** when the filter does not match any result.

        :param properties: List of properties to filter of.
        :type properties: dict.
        """
        return cls._filter(**restrictions).one()
