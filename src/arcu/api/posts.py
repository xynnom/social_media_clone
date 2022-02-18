import fastapi
from sqlalchemy.orm import Session
from ..db import auth, schemas, posts
from ..dependencies import get_db
from ..errors import base as error


router = fastapi.APIRouter()


@router.post("/api/posts", response_model=schemas.Post)
async def create_post(
    post: schemas.PostCreate,
    user: schemas.User = fastapi.Depends(auth.get_current_user),
    db: Session = fastapi.Depends(get_db)
    ):
    return await posts.create_post(user=user, post=post, db=db)


@router.get("/api/posts")
async def get_posts(
    user: schemas.User = fastapi.Depends(auth.get_current_user),
    db: Session = fastapi.Depends(get_db)
    ):
    return await posts.get_posts(user, db)


@router.get("/api/posts/{post_id}", status_code=200)
async def get_post(
    post_id: int,
    user: schemas.User = fastapi.Depends(auth.get_current_user),
    db: Session = fastapi.Depends(get_db)
    ):
    
    return await posts.get_post(post_id, user, db)


@router.delete("/api/posts/{post_id}", status_code=204)
async def delete_post(
    post_id: int,
    user: schemas.User = fastapi.Depends(auth.get_current_user),
    db: Session = fastapi.Depends(get_db)
    ):

    await posts.delete_post(post_id, user, db)

    return {"message", "Successfully Deleted"}


@router.put("/api/posts/{post_id}", status_code=201)
async def update_post(
    post_id: int,
    post: schemas.PostCreate,
    user: schemas.User = fastapi.Depends(auth.get_current_user),
    db: Session = fastapi.Depends(get_db)
    ):

    await posts.update_post(post_id, post, user, db)
    return {"message", "Successfully Updated"}
