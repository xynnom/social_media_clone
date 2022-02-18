import fastapi
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session
from . import users as user_db
from . import models, schemas
from ..dependencies import get_db
from ..errors.base import AuthUnauthorized
from ..config import get_settings


settings = get_settings()
oauth2schema = OAuth2PasswordBearer(tokenUrl="/api/token")


async def authenticate_user(
        username: str, 
        password: str, 
        db: Session = fastapi.Depends(get_db)
    ):

    user = await user_db.get_user(username, db)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user


async def create_token(user: schemas.User):
    user_obj = schemas.User.from_orm(user)

    token = jwt.encode(user_obj.dict(), settings.JWT_SECRET)

    return dict(access_token=token, token_type="bearer")


async def get_current_user(
        db: Session = fastapi.Depends(get_db),
        token: str = fastapi.Depends(oauth2schema),
    ):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        user = db.query(models.User).get(payload["id"])
    except:
        raise AuthUnauthorized
    return schemas.User.from_orm(user)