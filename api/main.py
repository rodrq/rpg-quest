from fastapi import FastAPI
from routers import character, quest
from database import Base, engine

def get_app() -> FastAPI:

    app = FastAPI()

    Base.metadata.create_all(bind=engine)
    
    app.include_router(character.router)

    app.include_router(quest.router)

    return app

app = get_app()



