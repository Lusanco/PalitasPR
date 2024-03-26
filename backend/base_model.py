#!/usr/bin/python3
""" BASE FOR ALL CLASSES"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()

class BaseModel:
    """
        BASE CLASS
    """

    id = Column(
        String(60),
        primary_key=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            self.set_attr(**kwargs)

    def set_attr(self, **kwargs):
        """Set attributes from a dictionary"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def all_columns(self):
        """
            Returns dict of columns and values in json
        """
        dict_of_table = {}

        # Ask obj for column names and the values thanks to Alchemy
        for column in self.__table__.columns:
            column_name = column.name
            column_value = getattr(self, column_name)
            dict_of_table[column_name] = column_value

        return dict_of_table