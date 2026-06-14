import httpx
from sqlalchemy.orm import Session
from app.models.opportunity import Opportunity, Category
from app.config import settings

async def fetch_jobs_from_adzuna(db: Session):
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1"
    params = {
        "app_id": settings.ADZUNA_APP_ID,
        "app_key": settings.ADZUNA_APP_KEY,
        "results_per_page": 10,
        "what": "internship",
        "content-type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()

    results = data.get("results", [])
    added = 0

    for job in results:
        title = job.get("title", "")
        description = job.get("description", "")
        link = job.get("redirect_url", "")

        existing = db.query(Opportunity).filter(Opportunity.link == link).first()
        if existing:
            continue

        new_opp = Opportunity(
            title=title,
            description=description,
            category=Category.internship,
            link=link,
            source="adzuna"
        )
        db.add(new_opp)
        added += 1

    db.commit()
    return added