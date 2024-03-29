from sqlalchemy.orm import Session
from src.models.models import Quest
from src.models.schemas import GetQuestsParams
from src.config.open_ai_model import openai_client
import json
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from src.utils.prompt import create_quest_prompt

async def create_quest_handler(username, class_, map, db: Session):
  try:
    system_prompt, user_prompt = create_quest_prompt(username, class_, map)
    completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format={ "type": "json_object" },
        temperature=1.0
    )
    result = json.loads(completion.choices[0].message.content)
    
    usage_tokens = completion.usage
    cost = (usage_tokens.prompt_tokens * 0.00001) + (usage_tokens.completion_tokens * 0.00003)
    
    quest = Quest(
        title=result['title'],
        description=result['description'],
        rewards=result['rewards'],
        experience=result['experience'],
        character_username=username,
        cost = cost
    ) 
    db.add(quest)
    db.commit()
    return JSONResponse(content={"quest": result})
    
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  
       
async def get_quests_handler(params: GetQuestsParams, db: Session):

  quests = db.query(Quest).filter(Quest.character_username == params.username).all()
  if not quests:
    raise HTTPException(status_code=404, detail=f"{params.username} didn't generate any quest yet.")
  quests_dict = [quest.__dict__ for quest in quests]
  return quests_dict

async def get_quest_handler(current_character_id, quest_id, db: Session):

      quest = db.query(Quest).filter_by(quest_id=quest_id, character_username=current_character_id).first()
      if not quest:
        raise HTTPException(status_code=401, detail="Invalid credentials")
      return quest

  