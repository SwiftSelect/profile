from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Recruiter(Base):
    __tablename__ = "recruiters"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    phone = Column(String, unique=True)
    current_position = Column(String)
    location = Column(String)