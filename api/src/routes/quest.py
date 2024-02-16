from fastapi import APIRouter, Depends
from src.controllers.quest import create_quest_handler, get_quests_handler, get_quest_handler
from src.models.schemas import QuestGenerationParams, GetQuestsParams, CharacterParams, QuestGenerationMap
from typing import Annotated
from src.auth.auth import get_current_character, get_current_character_id

router = APIRouter(prefix='/quest',
                   tags=['Quests'])

@router.post("/")
async def create_quest(current_character: Annotated[CharacterParams, Depends(get_current_character)], map:QuestGenerationMap):
    return await create_quest_handler(username = current_character.username, 
                                         class_= current_character.class_,
                                         map=map.map)


@router.get("/all")
async def get_quests(current_character_id: Annotated[GetQuestsParams, Depends(get_current_character_id)]):
    return await get_quests_handler(current_character_id)

@router.get("/{quest_id}")
async def get_quest(quest_id: int, current_character_id: Annotated[GetQuestsParams, Depends(get_current_character_id)]):
    return await get_quest_handler(current_character_id.username, quest_id)
    