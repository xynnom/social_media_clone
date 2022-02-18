from jose import JWTError, jwt
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..config import get_settings
from ..db import users, models
from ..dependencies import get_db
from ..db.schemas import JWTPayload, User, UserCreate
from ..errors.base import AuthUnauthorized


settings = get_settings()
router = APIRouter()
oauth2schema = OAuth2PasswordBearer(tokenUrl="/api/token")


async def authenticate_user(
    username: str, password: str, db: Session = Depends(get_db)):
    user = await users.get_user(username, db)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user


async def create_token(user: User):
    user_obj = User.from_orm(user)

    token = jwt.encode(user_obj.dict(), settings.JWT_SECRET)

    return dict(access_token=token, token_type="bearer")


async def get_current_user(
        db: Session = Depends(get_db),
        token: str = Depends(oauth2schema),
    ):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        user = db.query(models.User).get(payload["id"])
    except:
        raise AuthUnauthorized
    return User.from_orm(user)