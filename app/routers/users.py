from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UpdateInterests
from app.utils.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.patch("/me/interests")
def update_interests(data: UpdateInterests, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    current_user.interests = data.interests
    db.commit()
    return {"message": "Interests updated", "interests": data.interests}