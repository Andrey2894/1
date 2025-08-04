from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Department(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, primary_key=True, index=True)
    boss = Column(Integer, ForeignKey("users.id"), nullable=False)
    boss = relationship('User', remote_side=[id], back_populates='subordinates')
    number
    users