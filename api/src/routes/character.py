from fastapi import APIRouter
from src.models.schemas import CharacterParams
from src.controllers.character import create_character_handler




router = APIRouter(prefix='/character',
                   tags=['character'])


@router.post('/')
async def create_character(params: CharacterParams):
    return await create_character_handler(params)
    
    