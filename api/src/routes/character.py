from fastapi import APIRouter
from src.models.schemas import CharacterInDb
from src.handlers.character import create_character_handler



router = APIRouter(prefix='/character',
                   tags=['character'])


@router.post('/')
async def create_character(params: CharacterInDb):
    return await create_character_handler(params)
    
