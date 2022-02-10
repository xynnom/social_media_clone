from pydantic import BaseModel
from typing import List


class User(BaseModel):
    username: str
    role: str


class JWTPayload(BaseModel):
    username: str
    iss: str
    sub: str
    aud: str
    iat: int
    exp: int
    jti: str
    expiration: int


class UserSignupResponse(BaseModel):
    username: str
    role: str
