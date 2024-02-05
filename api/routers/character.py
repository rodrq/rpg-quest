from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.models import Character as CharacterModel
from db.init import engine

router = APIRouter()

class Character(BaseModel):
    name: str
    password: str
    class_: str

@router.post("/character")
async def create_character(character: Character):
    try:
        with Session(engine) as session:
            character_model = CharacterModel(
                name=character.name,
                password=character.password,
                class_=character.class_
            )

            session.add(character_model)
            session.commit()

        return {"message": "Character created successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))