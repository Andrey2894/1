from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

from api.models.enums.order_type import OrderType
from api.models.enums.order_status import OrderStatus
from api.models.enums.initiator_department import InitiatorDepartment

Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    entry_number = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    title = Column(String, nullable=False)

    file_id = Column(
        Integer,
        ForeignKey("files.id"),  # ссылаемся на таблицу files
        nullable=False,
        comment="FK к таблице files — прикреплённый файл",
    )
    file = relationship(
        "File",
        back_populates="orders",  # в File нужно определить orders = relationship("Order", back_populates="file")
        comment="Объект File, связанный с этим заказом",
    )

    created_at = Column(
        DateTime,
        nullable=False,
        comment="Дата создания заявки",
    )
    started_at = Column(
        DateTime,
        nullable=True,
        comment="Дата старта работы по заявке",
    )
    finished_at = Column(
        DateTime,
        nullable=True,
        comment="Дата завершения работы",
    )
    canceled_at = Column(
        DateTime,
        nullable=True,
        comment="Дата отмены заявки",
    )

    status = Column(Enum(OrderStatus), nullable=False)
    type = Column(Enum(OrderType), nullable=False)

    initiator_id = Column(
        Integer,
        ForeignKey("users.id"),  # ссылаемся на таблицу users
        nullable=False,
        comment="FK к таблице users — кто создал заявку",
    )
    initiator = relationship(
        "User",
        back_populates="orders",  # в User нужно определить orders = relationship("Order", back_populates="initiator")
        comment="Объект User — инициатор заявки",
    )

    initiator_department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    initiator_department = relationship("Department", back_populates="orders")

    thematic = Column(String, nullable=True)

    influence_on = Column(String, nullable=True)