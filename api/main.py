from fastapi import FastAPI
from routers import character, quest
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(character.router)
app.include_router(quest.router)

