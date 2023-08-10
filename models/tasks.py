from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)


class Task(BaseModel):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    key = Column(String(255), nullable=False)
    json = Column(Text, nullable=True)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return f'Task (id={self.id}, key={self.key})'
