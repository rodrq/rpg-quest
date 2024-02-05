from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from api.main import app
# Define the Pydantic model
class CharacterBase(BaseModel):
    name: str
    password: str
    class_: str

# Create the SQLAlchemy engine and session
engine = create_engine('postgresql://user:password@localhost/dbname')
Session = sessionmaker(bind=engine)

# Define the SQLAlchemy table
metadata = MetaData()
Character = Table(
    'character',
    metadata,
    Column('CharacterID', Integer, primary_key=True),
    Column('Name', String),
    Column('Password', String),
    Column('Class', String),
)


@app.post("/character")
async def create_character(character: CharacterBase):
    # Create a new SQLAlchemy session
    session = Session()

    # Insert the new character into the database
    session.execute(Character.insert().values(
        Name=character.name,
        Password=character.password,
        Class=character.class_
    ))

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()

    return {"message": "Character created successfully"}