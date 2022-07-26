from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from ..db import auth, schemas, users as user_db
from ..dependencies import get_db
from ..errors import base as error


router = APIRouter(
    prefix='/users'
)


@router.post("")
async def create_user(
    user: schemas.UserCreate,
    db: Session = fastapi.Depends(get_db)
    ):
    
    db_user = await user_db.get_user(user.username, db)
    if db_user:
        raise error.DuplicateItem
    
    await user_db.create_user(user, db)

    return await auth.create_token(user)


@router.post("")
async def generate_token(
    form_data: OAuth2PasswordRequestForm = fastapi.Depends(),
    db: Session = fastapi.Depends(get_db),
    ):
    
    user = await auth.authenticate_user(
        form_data.username, form_data.password, db
    )

    if not user:
        raise error.AuthUnauthorized

    return await auth.create_token(user)


@router.get("/me", response_model=schemas.User)
async def get_user(
    user: schemas.User = fastapi.Depends(auth.get_current_user)):
    return user