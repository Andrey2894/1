from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from typing import List

from app.db.session import get_db
from app.models.order import Order
from app.enums.order_status import OrderStatus
from app.schemas.order_schema import OrderCreate, OrderOut

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderOut)
async def create_order(payload: OrderCreate, db: AsyncSession = Depends(get_db)):
    order = Order(**payload.dict(exclude_none=True))
    order.status = OrderStatus.CREATED
    order.created_at = datetime.utcnow()
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order

@router.get("/", response_model=List[OrderOut])
async def get_orders(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Order))
    return result.scalars().all()

@router.put("/{order_id}/start", response_model=OrderOut)
async def start_order(order_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalars().first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = OrderStatus.IN_PROGRESS
    order.started_at = datetime.utcnow()
    await db.commit()
    await db.refresh(order)
    return order

@router.put("/{order_id}/finish", response_model=OrderOut)
async def finish_order(order_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalars().first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = OrderStatus.FINISHED
    order.finished_at = datetime.utcnow()
    await db.commit()
    await db.refresh(order)
    return order

@router.put("/{order_id}/cancel", response_model=OrderOut)
async def cancel_order(order_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalars().first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = OrderStatus.CANCELED
    order.canceled_at = datetime.utcnow()
    await db.commit()
    await db.refresh(order)
    return order
