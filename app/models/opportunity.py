from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from app.database import Base
import enum

class Category(str, enum.Enum):
    internship = "internship"
    hackathon = "hackathon"
    scholarship = "scholarship"
    job = "job"
    certification = "certification"

class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(Enum(Category), nullable=False)
    deadline = Column(DateTime(timezone=True), nullable=True)
    link = Column(String, nullable=False)
    source = Column(String, default="manual")
    created_at = Column(DateTime(timezone=True), server_default=func.now())