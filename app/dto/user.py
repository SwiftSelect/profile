from pydantic import BaseModel
from typing import Optional

class Org(BaseModel):
    id: int
    name: str
    domain: str

class User(BaseModel):
    id: int

class UserResponse(BaseModel):
    id: int
    email: str
    firstname: str
    lastname: str
    role_id: int
    org: Optional[Org]