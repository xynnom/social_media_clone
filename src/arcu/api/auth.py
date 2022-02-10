from jose import JWTError, jwt
from fastapi import Depends, APIRouter, HTTPException, status
from ..config import get_settings
from fastapi.security import OAuth2PasswordBearer

settings = get_settings()
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.authjwt_public_key,
                             audience=settings.authjwt_decode_audience,
                             algorithms=[settings.authjwt_algorithm])
    except JWTError:
        raise credentials_exception
    return payload


# Temporary token Verification endpoint
@router.post("/user/verify_test", tags=["auth"])
async def verify_user(payload: str = Depends(verify_token)):
    payload = payload
    return payload
