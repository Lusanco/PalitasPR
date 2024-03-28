#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base

class UserServiceAssoc(BaseModel, Base):
    __tablename__ = 'user_service_assoc'


    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    service_id = Column(String, ForeignKey('services.id'), nullable=False)
    town_id = Column(String, ForeignKey('towns.id'), nullable=False)

    # Relationships, this allows to call the related objects to a row on this table
    user = relationship('User')
    town = relationship('Town')
    service = relationship('Service')

    __table_args__ = (
        UniqueConstraint('user_id', 'service_id', 'town_id'),
    )

class Service(BaseModel, Base):
    __tablename__ = 'services'

    name = Column(String(50), nullable=False)

class User(BaseModel, Base):
    __tablename__ = 'users'

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)


class Town(BaseModel, Base):
    __tablename__ = 'towns'

    name = Column(String(50), nullable=False)
