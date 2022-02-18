from sqlalchemy.orm import Session
from .schemas import JWTPayload, UserCreate, User
from . import models
import passlib.hash as _hash


async def get_user(username: str, db: Session) -> User:
    db_user = \
        db.query(models.User).filter_by(username=username).first()
    return db_user


async def create_user(user: UserCreate, db: Session):
    db_user = models.User(
        username=user.username,
        hashed_password=_hash.bcrypt.hash(user.hashed_password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


