from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True
