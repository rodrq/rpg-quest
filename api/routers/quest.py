from fastapi import APIRouter
from pydantic import BaseModel
from controllers.quest import QuestGenerationParams, create_quest_handler
from sqlalchemy.orm import Session
from db.init import engine  # Assuming you have an engine for your database
from db.models import Quest 
router = APIRouter()


@router.post("/quest")
async def create_quest(params: QuestGenerationParams):
    return await create_quest_handler(params)


class GetQuests(BaseModel):
  character_name: str
  
@router.get("/quest")
async def get_quests(params: GetQuests):
  with Session(engine) as session:
    quests = session.query(Quest).filter(Quest.character_name == params.character_name).all()

  quests_dict = [quest.__dict__ for quest in quests]

  return quests_dictx
