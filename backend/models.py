#!/usr/bin/python3
"""
    All classes for tables(DataBase)
"""

from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base

class UserServiceAssoc(BaseModel, Base):
    __tablename__ = 'user_service_assoc'


    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    service_id = Column(String, ForeignKey('services.id'), nullable=False)
    town_id = Column(String, ForeignKey('towns.id'), nullable=False)

    """
        Relationships, this allows to call the related objects to a row on this table
        lazy=joined allows to load the objects from the relationships in ...
        same time you query from 'user_service_assoc'
    """
    user = relationship('User', cascade='all, delete', lazy='joined', back_populates='user_service_assoc')
    town = relationship('Town', cascade='all, delete', lazy='joined', back_populates='user_service_assoc')
    service = relationship('Service', cascade='all, delete', lazy='joined', back_populates='user_service_assoc')

    __table_args__ = (UniqueConstraint('user_id', 'service_id', 'town_id'),)

class CategoryServiceAssoc(BaseModel, Base):
    __tablename__ = 'categories_service_assoc'

    category_id = Column(String, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    service_id = Column(String, ForeignKey('services.id', ondelete='CASCADE'), nullable=False)

    category = relationship('Category', cascade='all, delete', lazy='joined')
    service = relationship('Service', cascade='all, delete', lazy='joined')

class Service(BaseModel, Base):
    __tablename__ = 'services'

    name = Column(String(50), unique=True, nullable=False)

    user_service_assoc = relationship('UserServiceAssoc', back_populates='service')

class User(BaseModel, Base):
    __tablename__ = 'users'

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    user_service_assoc = relationship('UserServiceAssoc', back_populates='user')


class Town(BaseModel, Base):
    __tablename__ = 'towns'

    name = Column(String(50), unique=True, nullable=False)

    user_service_assoc = relationship('UserServiceAssoc', back_populates='town')

class Category(BaseModel, Base):
    __tablename__ = 'categories'

    name = Column(String(50), unique=True, nullable=False)

