from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException

from blog import models, schemas, database, oauth2

from sqlalchemy.orm import Session

from blog.controllers import blog


# prefix help you to remove it from the route
router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)



# Get all blogs

#old way without controller
# @router.get('/', response_model=List[schemas.ShowBlog])
# def all(db: Session = Depends(database.get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


# Create a blog
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


# Delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.delete(id, db)

#Update blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


#Get one blog by id

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show_blog(id: int, response: Response, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
