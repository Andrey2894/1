from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class file(Base):
    id = Column(Integer, primary_key=True, index=True)
    title
    created_at
    user
    content_type