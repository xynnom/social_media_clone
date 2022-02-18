from fastapi import Depends, APIRouter
from fastapi import security
from sqlalchemy.orm import Session
from .auth import authenticate_user, create_token, get_current_user
from ..dependencies import get_db
from ..db import users
from ..db.schemas import JWTPayload, User, UserCreate
from ..errors.base import DuplicateItem, AuthUnauthorized

router = APIRouter()


@router.post("/api/users")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = await users.get_user(user.username, db)
    if db_user:
        raise DuplicateItem
    
    return await users.create_user(user, db)


@router.post("/api/token")
async def generate_token(
        form_data: security.OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db),
    ):
    
    user = await authenticate_user(
        form_data.username, form_data.password, db)

    if not user:
        raise AuthUnauthorized

    return await create_token(user)


@router.get("/api/users/me", response_model=User)
async def get_user(user: User = Depends(get_current_user)):
    return user