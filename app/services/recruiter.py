from app.dto.recruiter import RecruiterProfileCreate, RecruiterProfileResponse
from sqlalchemy.orm import Session
from app.models.recruiter import Recruiter
from app.dto.user import User
from fastapi import HTTPException

def create_profile(db: Session, user: User, data: RecruiterProfileCreate):
    profile = Recruiter(user_id=user.id, **data.dict())
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def fetch_profile(db: Session, user: User):
    profile = db.query(Recruiter).filter_by(user_id=user.id).first()
    if not profile:
        raise HTTPException(404, "Profile doesn't exist, please create one")
    return profile

def put_profile(db: Session, user: User, data: RecruiterProfileCreate):
    profile = db.query(Recruiter).filter_by(user_id=user.id).first()

    if not profile:
        profile = create_profile(db, user, data)
    else:
        for field, value in data.dict(exclude_unset=True).items():
            setattr(profile, field, value)
        db.commit()
        db.refresh(profile)
    return profile