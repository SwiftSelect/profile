from sqlalchemy.orm import Session
from app.dto.candidate import CandidateProfileResponse, CandidateProfile
from app.models.candidate import Candidate
from app.dto.user import User
from fastapi import HTTPException
from supabase import create_client, Client
import os
from fastapi.responses import JSONResponse
from app.services.kafka_producer import produce_profile_update

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv("SUPABASE_URL", ""),
    os.getenv("SUPABASE_KEY", "")
)

def create_profile(db: Session, data: CandidateProfile, user: User):
    profile = Candidate(
        user_id=user.id,
        current_position = data.currentPosition,
        location = data.location,
        links = data.links,
        demographics = data.demographics,
        resume_url = data.resumeUrl,
        skills = data.skills,
        phone = data.phone
    )
    
    db.add(profile)
    db.commit()
    db.refresh(profile)
    if data.resume_url:
        produce_profile_update(user.id, data.resume_url)
    return profile

def fetch_profile(db: Session, user: User):
    profile = db.query(Candidate).filter_by(user_id=user.id).first()
    if not profile:
        raise HTTPException(404, "Profile not found")
    return profile

def fetch_profile_by_id(db: Session, id: int):
    profile = db.query(Candidate).filter_by(id=id).first()
    if not profile:
        raise HTTPException(404, "Profile not found")
    return profile

def put_profile(db: Session, user: User, data: CandidateProfile):
    profile = db.query(Candidate).filter_by(user_id=user.id).first()

    if not profile:
        profile = create_profile(db, user=user, data=data)
    else:
        for field, value in data.dict(exclude_unset=True).items():
            setattr(profile, field, value)
    db.commit()
    db.refresh(profile)
    if data.resume_url:
        produce_profile_update(user.id, data.resume_url)
    return profile

def gen_signed_url(user: User, filename: str):
    file_path = f"resumes/{user.id}/{filename}"
    
    signed_url = supabase.storage.from_("resumes").create_signed_upload_url(file_path)
    
    return JSONResponse({
        "signed_url": signed_url["signed_url"],
        "token": signed_url["token"],
        "file_path": file_path
    })

def get_resume_signed_url(file_path: str):

    signed_url = supabase.storage.from_("resumes").create_signed_url(
        file_path,
        3600  
    )
    print(f"url: {signed_url}")
    return JSONResponse({
        "signed_url": signed_url["signedUrl"]
    })
