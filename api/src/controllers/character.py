from src.models.schemas import CharacterParams
from sqlalchemy.orm import Session
from src.config.database import engine
from src.models.models import Character
from src.utils.pw_hash import get_hashed_password
from fastapi import HTTPException


async def create_character_handler(params: CharacterParams):
    try:
        with Session(engine) as session:
            db_char_name= session.query(Character).filter(Character.name == params.name).first()
            if db_char_name:
                raise HTTPException(status_code=400, detail="Character name already exists")
            character = Character(
                name=params.name,
                password=get_hashed_password(params.password),
                class_=params.class_
            )
            session.add(character)
            session.commit()
            

            return {"message": "User registered successfully"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

    
    
