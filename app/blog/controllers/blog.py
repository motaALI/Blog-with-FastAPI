from sqlalchemy.orm import Session

from blog import models, schemas

from fastapi import status, Response, HTTPException

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs




def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    #check if id in query not found throw an error
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    # else delete a blog
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    # you can get body like this blog.update({'title': request.title, 'body': request.body}) or =>
    blog.update(request.dict())

    db.commit()

    return 'UPDATED'

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        # you can do this in one line of code => from fastapi import HTTPException
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available"}
         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog