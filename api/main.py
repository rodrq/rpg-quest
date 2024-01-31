from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from quest_gen import generate_quest

app = FastAPI()

class QuestGenerationParams(BaseModel):
    weapon_param: str
    map_param: str

@app.post("/generate-quest")
async def generate_quest_endpoint(params: QuestGenerationParams):
    try:
        result = generate_quest(params.weapon_param, params.map_param)
        return JSONResponse(content={"text": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
