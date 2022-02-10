from sqlalchemy import Column, ForeignKey, Integer, String, Time, Date, \
    DateTime, Boolean, Text
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    """User Model"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False, server_default='0')

    role = relationship('Role', backref='user')
    role_id = Column(Integer, ForeignKey('role.id'),
                     nullable=False)


class Role(Base):
    """Role Database Model"""

    __tablename__ = "role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False, unique=True)
