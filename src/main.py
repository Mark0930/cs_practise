from fastapi import FastAPI
from database import get_db
import models
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
import schema
from starlette import status
from typing import List

app = FastAPI()

@app.get("/")
async def root(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schema.User])
def create_user(user_post:schema.User, db:Session = Depends(get_db)):

    new_user = models.User(**user_post.model_dump(mode='json'))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
