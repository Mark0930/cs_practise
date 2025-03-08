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

@app.get('/{user_id}', response_model=schema.User)
def get_user(user_id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put('/{user_id}', response_model=schema.User)
def update_user(user_id:int, user_update:schema.UserUpdate, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id)
    if user.first() is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.update(user_update.model_dump(mode='json', exclude_none=True), synchronize_session=False)
    db.commit()
    return user.first()

@app.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id)
    if user.first() is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.delete(synchronize_session=False)
    db.commit()
