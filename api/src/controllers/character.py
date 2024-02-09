from src.models.schemas import CharacterParams
from sqlalchemy.orm import Session
from src.config.database import engine
from src.models.models import Character
from src.utils.pw_hash import get_hashed_password
from src.utils.query import db_query_value
from fastapi import HTTPException


async def create_character_handler(params: CharacterParams):
    try:
        if db_query_value(Character, Character.username, params.username):
                raise HTTPException(status_code=400, detail="Character username already exists")
        character = Character(
            username=params.username,
            password=get_hashed_password(params.password),
            class_=params.class_
        )
        with Session(engine) as session:  
            session.add(character)
            session.commit()
            return {"message": "User registered successfully"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

    
    
