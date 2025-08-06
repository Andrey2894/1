from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.enums.order_type import OrderType
from app.enums.order_status import OrderStatus
from app.models.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    entry_number = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    title = Column(String, nullable=False)

    file_id = Column(Integer, ForeignKey("files.id"), nullable=True)
    file = relationship("File", back_populates="order", uselist=False)

    created_at = Column(DateTime, nullable=False)
    started_at = Column(DateTime)
    finished_at = Column(DateTime)
    canceled_at = Column(DateTime)

    status = Column(Enum(OrderStatus), nullable=False)
    type = Column(Enum(OrderType), nullable=False)

    initiator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    initiator = relationship("User", back_populates="order", uselist=False, foreign_keys=[initiator_id])

    initiator_department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    initiator_department = relationship("Department", back_populates="order", uselist=False)

    thematic = Column(String)
    influence_on = Column(String)
