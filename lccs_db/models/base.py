#
# This file is part of LCCS-DB.
# Copyright (C) 2022 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#
"""Model Configuration."""

from datetime import datetime

from bdc_db.db import db
from sqlalchemy import Column, DateTime
from sqlalchemy_utils import TranslationHybrid

from ..config import Config

translation_hybrid = TranslationHybrid(current_locale=Config.I18N_LANGUAGES['current_locale'][0],
                                       default_locale=Config.I18N_LANGUAGES['default_locale'][0])


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
