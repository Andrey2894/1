from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class User(Base):
    __tablename__ = "users"

    id                 = Column(Integer, primary_key=True, index=True)
    email              = Column(String, nullable=False, unique=True)
    first_name         = Column(String, nullable=False)
    last_name          = Column(String, nullable=False)
    father_name        = Column(String)
    department_id      = Column(Integer, ForeignKey("departments.id"))
    department         = relationship(
        "Department",
        back_populates="users",
        foreign_keys=[department_id]
    )
    files              = relationship("File", back_populates="user")
    order              = relationship(
        "Order",
        back_populates="initiator",
        uselist=False,
        foreign_keys="[Order.initiator_id]"
    )
    boss_of_department = relationship(
        "Department",
        back_populates="boss",
        uselist=False,
        foreign_keys="[Department.boss_id]"
    )
