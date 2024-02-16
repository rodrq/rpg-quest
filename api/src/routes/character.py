from fastapi import APIRouter, Depends
from src.config.database import get_db
from src.models.schemas import CharacterInDb
from src.handlers.character import create_character_handler
from sqlalchemy.orm import Session

router = APIRouter(prefix='/character',
                   tags=['character'])


@router.post('/')
async def create_character(params: CharacterInDb, db: Session = Depends(get_db)):
    return await create_character_handler(params, db)
    
