from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.auth.auth import authenticate_character, create_access_token, get_current_character
from src.models.schemas import TokenParams, QuestGenerationParams
from typing import Annotated
from datetime import timedelta
from src.config.config import TOKEN_LIFETIME_MINUTES

router = APIRouter(prefix="/auth",
                   tags=["Authorization"])


@router.post("/", response_model=TokenParams)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> TokenParams:
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
    return TokenParams(access_token=access_token, token_type="bearer")


@router.get("/metest", response_model=QuestGenerationParams)
async def read_users_me(
    current_user: Annotated[QuestGenerationParams, Depends(get_current_character)]
):
    return current_user
    
