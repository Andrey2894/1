from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Department(Base):
    __tablename__ = "departments"

    id      = Column(Integer, primary_key=True, index=True)
    title   = Column(String, nullable=False, index=True)
    boss_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    boss    = relationship(
        "User",
        back_populates="boss_of_department",
        uselist=False,
        foreign_keys=[boss_id]
    )
    users   = relationship(
        "User",
        back_populates="department",
        foreign_keys="[User.department_id]"
    )
    order   = relationship(
        "Order",
        back_populates="initiator_department",
        uselist=False,
        foreign_keys="[Order.initiator_department_id]"
    )
