from pydantic import BaseModel

class RecruiterProfileCreate(BaseModel):
    full_name: str
    company_name: str

class RecruiterProfileResponse(RecruiterProfileCreate):
    id: int
    class Config:
        orm_mode = True
