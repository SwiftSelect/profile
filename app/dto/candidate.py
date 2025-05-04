from pydantic import BaseModel, Field
from typing import Optional, Dict

class CandidateProfile(BaseModel):
    location: Optional[str]
    currentPosition: Optional[str] = Field(alias="current_position")
    phone: Optional[str]
    resumeUrl: Optional[str] = Field(alias="resume_url")
    links: Optional[Dict[str, str]]
    skills: Optional[list[str]]
    demographics: Optional[Dict[str, str]]

class CandidateProfileResponse(BaseModel):
    id: int
    user_id: int
    location: Optional[str]
    currentPosition: Optional[str] = Field(alias="current_position")
    phone: Optional[str]
    resumeUrl: Optional[str] = Field(alias="resume_url")
    links: Optional[Dict[str, str]]
    skills: Optional[list[str]]
    demographics: Optional[Dict[str, str]]