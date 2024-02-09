from sqlalchemy.orm import Session
from src.config.database import engine 
from src.models.models import Quest 
from src.models.schemas import QuestGenerationParams, GetQuestsParams
from src.config.open_ai_model import client
import json
from fastapi.responses import JSONResponse
from fastapi import HTTPException


async def create_quest_handler(quest_params):
  try:
    system_prompt, user_prompt = create_quest_prompt(quest_params.username, quest_params.class_, quest_params.map)
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format={ "type": "json_object" },
        temperature=1.0
    )
    result = json.loads(completion.choices[0].message.content)

    quest = Quest(
        title=result['title'],
        description=result['description'],
        rewards=result['rewards'],
        experience=result['experience'],
        character_username=quest_params.username
    )

    with Session(engine) as session:
      session.add(quest)
      session.commit()
      return JSONResponse(content={"quest": result})
    
  except Exception as e:
    print(e)
    raise HTTPException(status_code=500, detail=str(e))
  
def create_quest_prompt(username: str, class_: str, map: str):
    system_prompt = f"""You are a gamemaster of a RPG game. 
                    "Your task is to create an object in JSON, that will represent
                    a very short and concise quest using the information they tell you about themselves.
                    The quest should only and only have the following attributes as JSON payload:
                    'title': a string representing the quest's title,
                    'description': a string describing the quest,
                    'rewards': a list of strings with the quest's rewards,
                    'experience': an integer representing the experience points gained from the quest,
         
                    Speak to the player directly and don't greet them. Start by the key 'title'.
                    The harder the quest difficulty, the higher the experience and rewards.
                    """
    user_prompt = f""""Hello gamemaster, My name is {username} and I'm a {class_}. I'm currently in the map {map}"""
    return system_prompt, user_prompt
       
async def get_quests_handler(params: GetQuestsParams):
  with Session(engine) as session:
    quests = session.query(Quest).filter(Quest.character_username == params.character_username).all()
    if not quests:
      raise HTTPException(status_code=404, detail=f"{params.character_username} didn't generate any quest yet.")
    quests_dict = [quest.__dict__ for quest in quests]
    return quests_dict

async def get_quest_handler(quest_id: int):
  with Session(engine) as session:
    quest = session.query(Quest).filter(Quest.quest_id == quest_id).first()
    if not quest:
      raise HTTPException(status_code=404, detail="Quest not found")
    return quest
  