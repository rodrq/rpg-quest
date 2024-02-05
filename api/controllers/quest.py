from pydantic import BaseModel
from ai_model import client
import json
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.init import engine
from db.models import Quest

class QuestGenerationParams(BaseModel):
  name: str
  class_: str
  map: str

async def create_quest_handler(params: QuestGenerationParams):
  try:
    system_prompt, user_prompt = create_quest_prompt(params.name, params.class_, params.map)
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
        character_name=params.name
    )

    with Session(engine) as session:
      session.add(quest)
      session.commit()
    print("create_quest_handler", completion.usage)
    print('generate_quest_endpoint result', result)
    return JSONResponse(content={"quest": result})
  except Exception as e:
    print(e)
    raise HTTPException(status_code=500, detail=str(e))
  
        
def create_quest_prompt(name: str, class_: str, map: str):
    system_prompt = f"""You are a gamemaster of a RPG game. 
                    "Your task is to create an object in JSON, that will represent
                    a very short and concise quest using the information they tell you about themselves.
                    The quest should only and only have the following attributes as JSON payload:
                    'title': a string representing the quest's title,
                    'description': a string describing the quest,
                    'rewards': a string listing the quest's rewards,
                    'experience': an integer representing the experience points gained from the quest,
         
                    Speak to the player directly and don't greet them. Start by the key 'title'.
                    """
    user_prompt = f""""Hello gamemaster, My name is {name} and I'm a {class_}. I'm currently in the map {map}"""
    return system_prompt, user_prompt
