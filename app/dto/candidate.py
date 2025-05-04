from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict

class CandidateProfile(BaseModel):
    location: Optional[str]
    currentPosition: Optional[str]
    phone: Optional[str]
    resumeUrl: Optional[str]
    links: Optional[Dict[str, str]]
    skills: Optional[list[str]]
    demographics: Optional[Dict[str, str]]

class CandidateProfileResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: int
    user_id: int
    location: Optional[str]
    current_position: Optional[str] = Field(alias="currentPosition")
    phone: Optional[str]
    resume_url: Optional[str] = Field(alias="resumeUrl")
    links: Optional[Dict[str, str]]
    skills: Optional[list[str]]
    demographics: Optional[Dict[str, str]]