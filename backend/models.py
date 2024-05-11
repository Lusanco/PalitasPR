#!/usr/bin/python3
"""
    All classes for tables(DataBase)
"""

from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base, BaseModelSerial
from flask_login import UserMixin
from datetime import datetime

# ASSOCIATION USER & SERVICE & TOWN CLASS
class Promo_Towns(BaseModel, Base):
    __tablename__ = 'promo_towns'

    promo_id = Column(String, ForeignKey('promotions.id'), nullable=False)
    town_id = Column(Integer, ForeignKey('towns.id'), nullable=False)

    __table_args__ = (UniqueConstraint('promo_id', 'town_id'),)

class Request_Towns(BaseModel, Base):
    __tablename__ = 'request_towns'

    request_id = Column(String, ForeignKey('requests.id'), nullable=False)
    town_id = Column(Integer, ForeignKey('towns.id'), nullable=False)

    __table_args__ = (UniqueConstraint('request_id', 'town_id'),)

# SERVICE CLASS (Serial)
class Service(BaseModelSerial, Base):
    __tablename__ = 'services'

    name = Column(String(50), unique=True, nullable=False)

# USER CLASS
class User(BaseModel, UserMixin, Base):
    __tablename__ = 'users'

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    verified = Column(Boolean, default=False)
    verification_token = Column(String(128), unique=True)
    profile_pic = Column(String(255)) # Testing with one folder here for AWS only profile
    # suspended = Column(Boolean, default=False)
    # banned = Column(Boolean, default=False)
    # status = Column(String(255), nullable=False, default='active')
    # expiration_date = Column(DateTime)
    # def is_active(self):
    #     """
    #     Returns True if the user is active (verified, not suspended, not banned, and not expired).
    #     """
    #     now = datetime.utcnow()
    #     return (
    #         self.verified  # Check if the user is verified
    #         and not self.suspended  # Check if the user is not suspended
    #         and not self.banned  # Check if the user is not banned
    #         and self.status == 'active'  # Check if the user's status is 'active'
    #         and (self.expiration_date is None or self.expiration_date > now)  # Check if the user's account is not expired
    #     )

# TOWN CLASS (Serial)
class Town(BaseModelSerial, Base):
    __tablename__ = 'towns'

    name = Column(String(50), unique=True, nullable=False)

class Review(BaseModel, Base):
    __tablename__ = 'reviews'

    description = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    pictures = Column(String(255))

class Task(BaseModel, Base):
    __tablename__ = 'tasks'

    receiver_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    provider_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    service_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    status = Column(String(255), nullable=False, default='open')
    description = Column(String(255), nullable=False)
    review_id = Column(String(255), ForeignKey('reviews.id'))

class Promotion(BaseModel, Base):
    __tablename__ = 'promotions'
    user_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    service_id = Column(String(255), ForeignKey('services.id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    price_min = Column(Integer, default=0)
    price_max = Column(Integer, default=0)
    pictures = Column(String(255))

class Request(BaseModel, Base):
    __tablename__ = 'requests'
    user_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    service_id = Column(String(255), ForeignKey('services.id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    pictures = Column(String())
