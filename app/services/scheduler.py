from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.opportunity import Opportunity
from app.models.user import User
from app.services.email_service import send_deadline_reminder
from datetime import datetime, timedelta

scheduler = AsyncIOScheduler()

async def send_deadline_reminders():
    db: Session = SessionLocal()
    try:
        now = datetime.utcnow()
        three_days_later = now + timedelta(days=3)

        upcoming = db.query(Opportunity).filter(
            Opportunity.deadline != None,
            Opportunity.deadline >= now,
            Opportunity.deadline <= three_days_later
        ).all()

        if not upcoming:
            return

        users = db.query(User).all()

        for user in users:
            if not user.interests:
                continue
            interests = [i.strip() for i in user.interests.split(",")]
            relevant = [opp for opp in upcoming if opp.category.value in interests]
            if relevant:
                await send_deadline_reminder(user.email, user.name, relevant)
    finally:
        db.close()

def start_scheduler():
    scheduler.add_job(send_deadline_reminders, "cron", hour=9, minute=0)
    scheduler.start()