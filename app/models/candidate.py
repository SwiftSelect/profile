from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    current_position = Column(String)
    location = Column(String)
    resume_url = Column(String)
    links = Column(JSON)
    demographics = Column(JSON)
    skills = Column(JSON)