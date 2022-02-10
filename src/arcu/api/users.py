from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from .auth import verify_token
from ..dependencies import get_db
from ..db import users
from ..db.schemas import JWTPayload, UserSignupResponse

router = APIRouter()


@router.post("/signup", tags=["users"], response_model=UserSignupResponse)
async def user_signup(db: Session = Depends(get_db),
                      payload: JWTPayload = Depends(verify_token)):

    query = users.user_signup(db, payload)
    
    return query
