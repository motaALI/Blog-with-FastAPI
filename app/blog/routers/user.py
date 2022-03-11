from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

from blog import models, schemas, database

from sqlalchemy.orm import Session


from blog.controllers import user

# instead of defining this tags in evry route you can actually define it inside APIRouter
router = APIRouter(
    prefix="/user",
    tags=["Users"]
)



# instead of defining this tags in evry route you can actually define it inside APIRouter

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


#Get user by id
@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)