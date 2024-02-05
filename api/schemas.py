from pydantic import BaseModel


class CharacterParams(BaseModel):
    name: str
    password: str
    class_: str


class GetQuestsParams(BaseModel):
    character_name: str

class QuestGenerationParams(BaseModel):
  name: str
  class_: str
  map: str