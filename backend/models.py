#!/usr/bin/python3
"""
    All classes for tables(DataBase)
"""

from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, Float
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base

# ASSOCIATION USER & SERVICE & TOWN CLASS
class UserServiceAssoc(BaseModel, Base):
    __tablename__ = 'user_service_assoc'


    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    service_id = Column(String, ForeignKey('services.id', ondelete='CASCADE'), nullable=False)
    town_id = Column(String, ForeignKey('towns.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    user = relationship(
        'User',
        lazy='subquery',
        back_populates='user_service_assoc'
        )

    town = relationship(
        'Town',
        lazy='subquery',
        back_populates='user_service_assoc'
        )

    service = relationship(
        'Service',
        lazy='subquery',
        back_populates='user_service_assoc'
        )

    __table_args__ = (UniqueConstraint('user_id', 'service_id', 'town_id'),)


# SERVICE CLASS
class Service(BaseModel, Base):
    __tablename__ = 'services'

    name = Column(String(50), unique=True, nullable=False)

    # Relationships
    user_service_assoc = relationship(
        'UserServiceAssoc',
        back_populates='service'
        )

# USER CLASS
class User(BaseModel, Base):
    __tablename__ = 'users'

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    # Relationships
    user_service_assoc = relationship(
        'UserServiceAssoc',
        back_populates='user',
        cascade='all, delete'
        )

# TOWN CLASS
class Town(BaseModel, Base):
    __tablename__ = 'towns'

    name = Column(String(50), unique=True, nullable=False)

    # Relationships
    user_service_assoc = relationship(
        'UserServiceAssoc',
        back_populates='town',
        cascade='all, delete'
        )
    
# Task Class
class Task(BaseModel, Base):
    __tablename__ = 'tasks'

    # Columns
    id = Column(String, primary_key=True)
    provider_id = Column(String, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(String, ForeignKey('users.id'), nullable=False)
    service_id = Column(String, ForeignKey('services.id'), nullable=False)
    status = Column(String, nullable=False)
    review = Column(String)
    rating = Column(Float)

    # Relationships
    provider = relationship('User', foreign_keys=[provider_id])
    receiver = relationship('User', foreign_keys=[receiver_id])
    service = relationship('Service')

    def __repr__(self):
        return f"<Task(id={self.id}, status={self.status}, rating={self.rating})>"