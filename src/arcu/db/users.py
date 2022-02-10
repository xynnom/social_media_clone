from sqlalchemy.orm import Session
from .schemas import JWTPayload
from . import models
from ..errors.base import DuplicateItem


def user_signup(db: Session, user_dict: JWTPayload):

    user = {"username": user_dict['username']}
    # Check if username already exists.
    db_user = \
        db.query(models.User).filter_by(username=user['username']).first()
    if db_user:
        raise DuplicateItem

    # Check if there are roles. For now, the default is "admin".
    user_role = db.query(models.Role).filter_by(name='admin').first()
    if not user_role:
        user_role = models.Role(name='admin')
        db.add_all([
            user_role,
            models.Role(name='user'),
        ])
        db.commit()

    user = models.User(**user, role=user_role)
    db.add(user)
    db.commit()

    result = {
        "username": user.username,
        "role": user.role.name
    }

    return result
