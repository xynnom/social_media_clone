import passlib.hash as _hash
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime as dt
from .database import Base


class User(Base):
    """User Model"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True, index=True)
    is_active = Column(Boolean, nullable=False, server_default='0')
    hashed_password = Column(String)

    posts = relationship("Post", back_populates="owner")
    comments = relationship("Comment", back_populates="owner") 

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)
    
    
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_message = Column(String(125), index=True)
    date_created = Column(DateTime, default=dt.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner =  relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="parent") 


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    comment = Column(String(125), index=True)
    date_created = Column(DateTime, default=dt.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))
    parent_id = Column(Integer, ForeignKey("posts.id"))

    owner =  relationship("User", back_populates="comments")
    parent  =  relationship("Post", back_populates="comments")

