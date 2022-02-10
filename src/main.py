from arcu.api import auth
from arcu.api import users
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from arcu.db import models
from arcu.db.database import engine


models.Base.metadata.create_all(bind=engine)

 
tags_metadata = [
    {
        "name": "soc_med",
        "description": "This is a social media clone.",
    }
]

app = FastAPI(
    title="Arc-U Backend",
    description="A REST API server that return information about datasets.",
    version="0.0.1",
    openapi_tags=tags_metadata)

# register of Endpoints
app.include_router(auth.router)
app.include_router(users.router)

# CORS
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Arc-U"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )
