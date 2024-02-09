from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from src.auth.auth import authenticate_character, create_access_token, get_current_character
from typing import Annotated
from datetime import timedelta
from src.config.config import TOKEN_LIFETIME_MINUTES
router = APIRouter(prefix="/auth",
                   tags=["Authorization"])


@router.post("/")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_character(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(TOKEN_LIFETIME_MINUTES))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response = JSONResponse(content={"message": "Login succesfull"})
    response.set_cookie(key="token", value=access_token, max_age=1800)
    return response



    
