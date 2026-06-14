from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class Category(str, Enum):
    internship = "internship"
    hackathon = "hackathon"
    scholarship = "scholarship"
    job = "job"
    certification = "certification"

class OpportunityCreate(BaseModel):
    title: str
    description: str
    category: Category
    deadline: Optional[datetime] = None
    link: str

class OpportunityResponse(BaseModel):
    id: int
    title: str
    description: str
    category: Category
    deadline: Optional[datetime]
    link: str
    source: str
    created_at: datetime

    class Config:
        from_attributes = True