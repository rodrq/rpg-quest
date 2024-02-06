from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Character(Base):
    __tablename__ = 'characters'
    
    name = Column(String, primary_key=True)
    password = Column(String)
    class_ = Column(String, name="class")
    quests = relationship('Quest', back_populates='character')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Quest(Base):
    __tablename__ = 'quests'
    
    quest_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    rewards = Column(String)
    experience = Column(Integer)
    character_name = Column(String, ForeignKey('characters.name'))
    character = relationship('Character', back_populates='quests')
