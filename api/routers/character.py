from fastapi import APIRouter
from schemas import CharacterParams
from sqlalchemy.orm import Session
from database import engine
from db.models import Character
from auth.utils import get_hashed_password
from fastapi import HTTPException

router = APIRouter(prefix='/character',
                   tags=['character'])


@router.post('/')
async def create_character(params: CharacterParams):
    try:
        with Session(engine) as session:
            db_char_name= session.query(Character).filter(Character.name == params.name).first()
            if db_char_name:
                raise HTTPException(status_code=400, detail="Character name already exists")
            character_model = Character(
                name=params.name,
                password=get_hashed_password(params.password),
                class_=params.class_
            )
            session.add(character_model)
            session.commit()
            return {"message": "User registered successfully"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

    
    
