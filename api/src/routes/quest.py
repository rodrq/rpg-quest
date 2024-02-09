from fastapi import APIRouter, Depends
from src.controllers.quest import create_quest_handler, get_quests_handler, get_quest_handler
from src.models.schemas import QuestGenerationParams, GetQuestsParams, CharacterParams, QuestGenerationMap
from typing import Annotated
from src.auth.auth import get_current_character

router = APIRouter(prefix='/quest',
                   tags=['Quests'])

@router.post("/")
async def create_quest(current_character: Annotated[CharacterParams, Depends(get_current_character)], map:QuestGenerationMap):
    quest_params = QuestGenerationParams(username = current_character.username, 
                                         class_= current_character.class_,
                                         map=map.map)
    print(quest_params)
    return await create_quest_handler(quest_params)

@router.get('/quest-params', response_model=QuestGenerationParams)
async def get_character_params(current_character: Annotated[CharacterParams, Depends(get_current_character)], map:QuestGenerationMap):
    quest_params = QuestGenerationParams(username = current_character.username, 
                                         class_= current_character.class_,
                                         map=map.map)
    return quest_params
@router.get("/")
async def get_quests(params: GetQuestsParams):
    return await get_quests_handler(params)


####MEJORAR SEGURIDAD CUALQUIER VE TODO. 
@router.get("/{quest_id}")
async def get_quest(quest_id: int):
    return await get_quest_handler(quest_id)