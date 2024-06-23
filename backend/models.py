"""
    All classes for tables(DataBase)
"""

from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, Integer, Boolean,  Index
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base, BaseModelSerial
from sqlalchemy.dialects.postgresql import TSVECTOR
from flask_login import UserMixin


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

class User(BaseModel, UserMixin, Base):
    __tablename__ = "users"

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    verified = Column(Boolean, default=False)
    verification_token = Column(String(128), unique=True)

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

class Initial_Contact(BaseModel, Base):
    __tablename__ = 'initial_contacts'

    receiver_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    receiver_read = Column(Boolean, default=False)
    sender_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    sender_read = Column(Boolean, default=False)
    promo_id = Column(String(255), ForeignKey("promotions.id"))
    sent_task = Column(Boolean, default=False)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])
    promo = relationship("Promotion", foreign_keys=[promo_id])

class Task(BaseModel, Base):
    __tablename__ = "tasks"
    initial_contact_id = Column(String(255), ForeignKey("initial_contacts.id"), nullable=False)
    promo_id = Column(String(50), ForeignKey('promotions.id'))
    request_id = Column(String(50), ForeignKey('requests.id'))
    receiver_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    receiver_confirm = Column(Boolean)
    provider_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    service_id = Column(String(255), ForeignKey("users.id"), nullable=False)
    status = Column(String(255), nullable=False, default="pending")
    description = Column(String(255), nullable=False)
    price = Column(Integer)

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

    user = relationship('User', foreign_keys=[user_id])


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

    user = relationship('User', foreign_keys=[user_id])