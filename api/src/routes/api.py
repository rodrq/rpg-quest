from fastapi import APIRouter
from . import auth, character, quest

router = APIRouter()

router.include_router(character.router)

router.include_router(quest.router)

router.include_router(auth.router)