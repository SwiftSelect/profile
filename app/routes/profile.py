from app.utils.get_user_from_auth import get_user_from_auth
from app.services.candidate import fetch_profile as get_cand_profile, create_profile as create_cand_profile, put_profile as put_cand_profile, gen_signed_url, get_resume_signed_url
from app.services.recruiter import fetch_profile as get_rec_profile, create_profile as create_rec_profile, put_profile as put_rec_profile
from app.services.candidate import fetch_profile_by_id as get_cand_profile_by_id
from fastapi import HTTPException, APIRouter, Depends, Header
from app.enums.roles import Roles
from sqlalchemy.orm import Session
from app.database import get_db
from app.dto.candidate import CandidateProfileResponse, CandidateProfile
from app.dto.recruiter import RecruiterProfileResponse
from typing import Optional, Dict

router = APIRouter()

@router.get("/", response_model=CandidateProfileResponse | RecruiterProfileResponse)
def get_profile(db: Session = Depends(get_db), authorization: Optional[str] = Header(None)):
    user = get_user_from_auth(authorization)
    if user.role_id== Roles.CANDIDATE.value:
        return get_cand_profile(user=user,  db=db)
    else:
        return get_rec_profile(user=user,  db=db)
    
@router.get("/{id}", response_model=CandidateProfileResponse)
def get_profile_by_id(id: int, db: Session = Depends(get_db)):
    return get_cand_profile_by_id(id=id, db=db)
    
@router.post("/")
def create_candidate_profile(
    data: CandidateProfile,
    db: Session = Depends(get_db),
    authorization: Optional[str] = Header(None)
):
    user = get_user_from_auth(authorization)
    if user.role_id == Roles.CANDIDATE.value:
        return create_cand_profile(user=user,  db=db, data=data)
    else:
        return create_rec_profile(user=user,  db=db, data=data)
    
@router.put("/", response_model=CandidateProfileResponse)
def update_profile(data: CandidateProfile, db: Session = Depends(get_db), authorization: Optional[str] = Header(None)):
    user = get_user_from_auth(authorization)
    print(f"user, HERE: {user}")
    if user.role_id == Roles.CANDIDATE.value:
        return put_cand_profile(user=user,  db=db, data=data)
    else:
        return put_rec_profile(user=user,  db=db, data=data)
    
@router.get("/resume-upload-url/{filename}")
def get_resume_upload_url(filename: str, authorization: Optional[str] = Header(None)):
    user = get_user_from_auth(authorization)
    if user.role_id != Roles.CANDIDATE.value:
        raise HTTPException(403, "Should not generate resume url for role RECRUITER")
    return gen_signed_url(user=user, filename=filename)

@router.get("/resume-view-url")
def get_resume_view_url(filePath: str, authorization: Optional[str] = Header(None)):
    user = get_user_from_auth(authorization)
    # Both candidates and recruiters should be able to view resumes
    return get_resume_signed_url(filePath)