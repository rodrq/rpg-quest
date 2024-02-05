from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from quest_gen import generate_quest

app = FastAPI()

class QuestGenerationParams(BaseModel):
    name: str
    class_: str
    map: str

@app.post("/quest")
async def generate_quest_endpoint(params: QuestGenerationParams):
    try:
        result = generate_quest(params.name, params.class_, params.map)
        return JSONResponse(content={"text": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

