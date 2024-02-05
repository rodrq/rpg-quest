from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'
    
    name = Column(String, primary_key=True)
    password = Column(String)
    class_ = Column(String, name="class")
    quests = relationship('Quest', back_populates='character')

class Quest(Base):
    __tablename__ = 'quests'
    
    quest_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    rewards = Column(String)
    experience = Column(Integer)
    character_name = Column(String, ForeignKey('characters.name'))
    character = relationship('Character', back_populates='quests')
