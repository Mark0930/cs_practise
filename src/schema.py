from pydantic import BaseModel
from typing import Optional
from pydantic.networks import EmailStr

class User(BaseModel):
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

    class Config:
        from_attributes = True
