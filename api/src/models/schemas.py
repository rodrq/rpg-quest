from pydantic import BaseModel
from typing import Union


class TokenParams(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: Union[str, None] = None
    
class CharacterParams(BaseModel):
    username: str
    class_: str

class CharacterInDb(CharacterParams):
    password: str

class GetQuestsParams(BaseModel):
    character_username: str
    
class QuestGenerationMap(BaseModel):
    map: str
    
class QuestGenerationParams(BaseModel):
  username: str
  class_: str
  map: str = None