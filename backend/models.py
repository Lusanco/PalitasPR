#!/usr/bin/python3
"""
    All classes for tables(DataBase)
"""

from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, Integer, Boolean,  Index
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base, BaseModelSerial
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.event import listen
from sqlalchemy.sql import text


# ASSOCIATION USER & SERVICE & TOWN CLASS
class Promo_Towns(BaseModel, Base):
    __tablename__ = "promo_towns"

    promo_id = Column(String, ForeignKey("promotions.id"), nullable=False)
    town_id = Column(Integer, ForeignKey("towns.id"), nullable=False)

    __table_args__ = (UniqueConstraint("promo_id", "town_id"),)


class Request_Towns(BaseModel, Base):
    __tablename__ = "request_towns"

    request_id = Column(String, ForeignKey("requests.id"), nullable=False)
    town_id = Column(Integer, ForeignKey("towns.id"), nullable=False)

    __table_args__ = (UniqueConstraint("request_id", "town_id"),)


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    tsv = Column(TSVECTOR)

    __table_args__ = (
        Index('idx_services_tsv', 'tsv', postgresql_using='gin'),
    )


# USER CLASS
class User(BaseModel, UserMixin, Base):
    __tablename__ = "users"

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    verified = Column(Boolean, default=False)
    verification_token = Column(String(128), unique=True)

# TOWN CLASS (Serial id int)
class Town(BaseModelSerial, Base):
    __tablename__ = "towns"

    name = Column(String(50), unique=True, nullable=False)


class Review(BaseModel, Base):
    __tablename__ = "reviews"

    user_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    task_id = Column(String, nullable=False)
    description = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    pictures = Column(String(255))

    reviewer = relationship("User", foreign_keys=[user_id])

# W)RKING DOWN HERE NEED TESTING
class Initial_Contact(BaseModel, Base):
    __tablename__ = 'initial_contacts'

    receiver_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    sender_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    promo_id = Column(String(255), ForeignKey("promotions.id"), nullable=False)
    read = Column(Boolean, default=False)
    sent_task = Column(Boolean, default=False)

    # Relationships
    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])
    promo = relationship("Promotion", foreign_keys=[promo_id])


class Task(BaseModel, Base):
    __tablename__ = "tasks"
    initial_contact_id = Column(String(255), ForeignKey("initial_contacts.id"), nullable=False)
    promo_id = Column(String(50), ForeignKey('promotions.id'))
    receiver_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    receiver_confirm = Column(Boolean)
    provider_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    service_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    is_read = Column(Boolean, default=False)
    status = Column(String(255), nullable=False, default="open")
    description = Column(String(255), nullable=False)

    promo = relationship('Promotion', foreign_keys=[promo_id])

class Promotion(BaseModel, Base):
    __tablename__ = "promotions"
    user_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    service_id = Column(String(255), ForeignKey("services.id"), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    price_min = Column(Integer, default=0)
    price_max = Column(Integer, default=0)
    pictures = Column(String(255))

    user = relationship('User', foreign_keys=[user_id])


class Request(BaseModel, Base):
    __tablename__ = "requests"
    user_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    service_id = Column(String(255), ForeignKey("services.id"), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    pictures = Column(String())


class Profile(BaseModel, Base):
    __tablename__ = "profiles"

    id = Column(String(50), ForeignKey("users.id"), primary_key=True)
    user_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    job_title = Column(String(50))
    bio = Column(String)
    tasks_completed = Column(Integer)
    social_links = Column(String)
    profile_pic = Column(String(255))
    cover_pic = Column(String(255))
    gallery = Column(String(255))

    # relationships
    user = relationship('User', foreign_keys=[user_id])