from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.handlers.auth import login_for_access_token_handler
from typing import Annotated

router = APIRouter(prefix="/auth",
                   tags=["Authorization"])


@router.post("/")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return login_for_access_token_handler(form_data)
    



    
