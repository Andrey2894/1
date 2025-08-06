from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    content_type = Column(String, nullable=False)
    initiator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    url = Column(String, nullable=False)

    user = relationship("User", back_populates="files")
    order = relationship("Order", back_populates="file", uselist=False)
