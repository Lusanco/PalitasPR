#!/usr/bin/python3
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
import uuid

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
        DateTime(timezone=True),  # Adjusted for timezone
        nullable=False,
        default=func.now()  # Use database's current timestamp function
    )

    updated_at = Column(
        DateTime(timezone=True),  # Adjusted for timezone
        nullable=False,
        default=func.now(),  # Use database's current timestamp function
        onupdate=func.now()  # Use database's current timestamp function for updates
    )

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
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
