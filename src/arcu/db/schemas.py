from pydantic import BaseModel
from typing import Optional
from datetime import datetime

import pydantic as _pydantic


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    hashed_password: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class JWTPayload(BaseModel):
    username: str
    iss: str
    sub: str
    aud: str
    iat: int
    exp: int
    jti: str
    expiration: int


class PostBase(BaseModel):
    post_message: str


class Post(PostBase):
    id: int
    owner_id: int
    date_created: datetime

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass

class CommentBase(BaseModel):
    comment_message: str


class Comment(CommentBase):
    id: int
    owner_id: int
    parent_id: int  # parent post
    date_created: datetime
    
    class Config:
        orm_mode = True
        
class CommentCreate(CommentBase):
    pass
