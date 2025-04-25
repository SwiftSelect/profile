from pydantic import BaseModel
from typing import Optional, Dict

class CandidateProfile(BaseModel):
    location: Optional[str]
    current_position: Optional[str]
    resume_url: Optional[str]
    links: Optional[Dict[str, str]]
    skills: Optional[list[str]]
    demographics: Optional[Dict[str, str]]

class CandidateProfileResponse(CandidateProfile):
    id: int
    class Config:
        orm_mode = True