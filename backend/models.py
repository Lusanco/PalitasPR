#!/usr/bin/python3
"""
    CLASSES FOR THE MOCKUP
    ONLY USER AND SERVICE AT THE MOMENT
"""

from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base


# Define association table for many-to-many relationship
user_service_association = Table(
    'user_service_association', Base.metadata,
    Column('user_id', String, ForeignKey('users.id')),
    Column('service_id', String, ForeignKey('services.id'))
)

class Service(BaseModel, Base):
    __tablename__ = 'services'

    name = Column(String(50), nullable=False)

    # Define relationship with User class, this is another table
    users = relationship("User", secondary=user_service_association, back_populates="services")

class User(BaseModel, Base):
    __tablename__ = 'users'

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    
    # Define relationship with Service class, this is another table
    services = relationship("Service", secondary=user_service_association, back_populates="users")