from sqlalchemy.orm import Session

from blog import models, schemas

from fastapi import status, HTTPException

from blog.hashing import Hash


def create(request: schemas.Blog, db: Session):
    #  hashedPassword = pwd_context.hash(request.password) # moved to hashing.py class
    new_user = models.User(username = request.username, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"User not available")
    return user