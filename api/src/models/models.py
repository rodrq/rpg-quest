from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from src.config.database import Base

class Character(Base):
    __tablename__ = 'characters'
     
    username = Column(String, primary_key=True, name='username', nullable=False, unique=True)
    password = Column(String, name='password', nullable=False)
    class_ = Column(String, name="class", nullable=False)
    quests = relationship('Quest', back_populates='character')
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    
    @validates('username', 'password', 'class_')
    def validate_not_empty(self, key, value):
        if not value or value.isspace():
            raise ValueError(f"{key} cannot be empty")
        print(f'{key} = {value} good')
        return value

    

class Quest(Base):
    __tablename__ = 'quests'
    
    quest_id = Column(Integer, primary_key=True)
    title = Column(String, name='title')
    description = Column(String, name='description')
    rewards = Column(String, name='rewards')
    experience = Column(Integer, name='experience')
    character_username = Column(String, ForeignKey('characters.username'))
    character = relationship('Character', back_populates='quests')
    cost = Column(Float, name="cost")
