from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email
    first_name
    last_name
    father_name
    department
