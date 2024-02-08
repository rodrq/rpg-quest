from fastapi import APIRouter
from src.controllers.quest import create_quest_handler, get_quests_handler, get_quest_handler
from src.models.schemas import QuestGenerationParams, GetQuestsParams

router = APIRouter(prefix='/quest',
                   tags=['Quests'])

@router.post("/")
async def create_quest(params: QuestGenerationParams):
    return await create_quest_handler(params)

@router.get("/")
async def get_quests(params: GetQuestsParams):
    return await get_quests_handler(params)


####MEJORAR SEGURIDAD CUALQUIER VE TODO. 
@router.get("/{quest_id}")
async def get_quest(quest_id: int):
    return await get_quest_handler(quest_id)