from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Recruiter(Base):
    __tablename__ = "recruiters"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    full_name = Column(String)
    company_name = Column(String)
