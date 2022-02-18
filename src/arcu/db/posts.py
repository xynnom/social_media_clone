from datetime import datetime
from sqlalchemy.orm import Session
from . import models, schemas


async def create_post(user: models.User, post: schemas.Post, db: Session):
    db_post = models.Post(**post.dict(), owner_id=user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


async def get_posts(user: models.User, db: Session):
    db_posts = db.query(models.Post).filter_by(owner_id=user.id)

    return list(map(schemas.Post.from_orm, db_posts))


async def _get_specific_post(post_id: int, user: models.User, db: Session):
    db_post = db.query(models.Post).filter_by(owner_id=user.id). \
        filter(models.Post.id == post_id).first()
    return db_post


async def get_post(post_id: int, user: models.User, db: Session):
    db_post = await _get_specific_post(post_id, user, db)

    return schemas.Post.from_orm(db_post)

async def delete_post(post_id: int, user: models.User, db: Session):
    db_post = await _get_specific_post(post_id, user, db)
    db.delete(db_post)
    db.commit()


async def update_post(
    post_id: int,
    post: schemas.PostCreate,
    user: models.User,
    db: Session
    ):

    db_post = await _get_specific_post(post_id, user, db)
    
    db_post.post_message = post.post_message
    db_post.date_updated = datetime.utcnow()

    db.commit()
    db.refresh(db_post)
    
    return schemas.Post.from_orm(db_post)
    