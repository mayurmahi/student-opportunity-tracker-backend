from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.opportunity import Opportunity, Category
from app.models.user import User
from app.schemas.opportunity import OpportunityCreate, OpportunityResponse
from app.utils.auth import get_current_user, get_admin_user
from app.services.opportunity_fetcher import fetch_jobs_from_adzuna
from app.services.scheduler import send_deadline_reminders

router = APIRouter(prefix="/opportunities", tags=["Opportunities"])

@router.post("/", response_model=OpportunityResponse)
def create_opportunity(opp: OpportunityCreate, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    new_opp = Opportunity(**opp.dict())
    db.add(new_opp)
    db.commit()
    db.refresh(new_opp)
    return new_opp

@router.get("/", response_model=List[OpportunityResponse])
def get_opportunities(category: Optional[Category] = None, search: Optional[str] = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    query = db.query(Opportunity)
    if category:
        query = query.filter(Opportunity.category == category)
    if search:
        query = query.filter(Opportunity.title.ilike(f"%{search}%"))
    return query.order_by(Opportunity.created_at.desc()).all()

@router.get("/recommended", response_model=List[OpportunityResponse])
def get_recommended(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.interests:
        raise HTTPException(status_code=400, detail="Please set your interests first")
    interests = [i.strip() for i in current_user.interests.split(",")]
    query = db.query(Opportunity).filter(Opportunity.category.in_(interests))
    return query.order_by(Opportunity.created_at.desc()).all()

@router.get("/{opp_id}", response_model=OpportunityResponse)
def get_single(opp_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    opp = db.query(Opportunity).filter(Opportunity.id == opp_id).first()
    if not opp:
        raise HTTPException(status_code=404, detail="Not found")
    return opp

@router.put("/{opp_id}", response_model=OpportunityResponse)
def update_opportunity(opp_id: int, opp: OpportunityCreate, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    existing = db.query(Opportunity).filter(Opportunity.id == opp_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Not found")
    for key, value in opp.dict().items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return existing

@router.delete("/{opp_id}")
def delete_opportunity(opp_id: int, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    opp = db.query(Opportunity).filter(Opportunity.id == opp_id).first()
    if not opp:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(opp)
    db.commit()
    return {"message": "Deleted successfully"}


@router.post("/fetch-from-api")
async def fetch_opportunities(db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    added = await fetch_jobs_from_adzuna(db)
    return {"message": f"{added} new opportunities added from Adzuna"}


@router.post("/test-reminder")
async def test_reminder(admin: User = Depends(get_admin_user)):
    await send_deadline_reminders()
    return {"message": "Reminder emails sent if any deadlines in next 3 days"}