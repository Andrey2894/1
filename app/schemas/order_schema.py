from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.enums.order_type import OrderType
from app.enums.order_status import OrderStatus

class OrderCreate(BaseModel):
    entry_number: str
    name: str
    title: str
    file_id: Optional[int] = None
    type: OrderType
    initiator_id: int
    initiator_department_id: int
    thematic: Optional[str] = None
    influence_on: Optional[str] = None

class OrderOut(BaseModel):
    id: int
    entry_number: str
    name: str
    title: str
    file_id: Optional[int]
    created_at: datetime
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    canceled_at: Optional[datetime] = None
    status: OrderStatus
    type: OrderType
    initiator_id: int
    initiator_department_id: int
    thematic: Optional[str] = None
    influence_on: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
