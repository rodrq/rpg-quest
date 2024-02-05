from fastapi import APIRouter
from pydantic import BaseModel
from controllers.quest import QuestGenerationParams, create_quest_handler
from sqlalchemy.orm import Session
from database import engine 
from db.models import Quest 
from schemas import GetQuestsParams
router = APIRouter()

@router.post("/quest")
async def create_quest(params: QuestGenerationParams):
    return await create_quest_handler(params)



  
@router.get("/quest")
async def get_quests(params: GetQuestsParams):
  with Session(engine) as session:
    quests = session.query(Quest).filter(Quest.character_name == params.character_name).all()

  quests_dict = [quest.__dict__ for quest in quests]
  return quests_dict
