from fastapi import APIRouter, HTTPException
from schemas import CharacterParams
from sqlalchemy.orm import Session
from db.models import Character
from database import engine
from auth.utils import get_hashed_password

router = APIRouter()


@router.post("/character")
async def create_character(character: CharacterParams):
    try:
        with Session(engine) as session:
            db_char_name= session.query(Character).filter(Character.name == character.name).first()
            if db_char_name:
                raise HTTPException(status_code=400, detail="Character name already exists")
            character_model = Character(
                name=character.name,
                password=get_hashed_password(character.password),
                class_=character.class_
            )
            session.add(character_model)
            session.commit()
            return {"message": "User registered successfully"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
