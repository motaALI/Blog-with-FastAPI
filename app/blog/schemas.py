from pydantic import BaseModel
from typing import List, Optional



class BlogBase(BaseModel):
    title: str
    body:str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class PostBlog(BlogBase):
    pass

class User(BaseModel):
    username: str
    email: str
    password: str

# create the request model cause we don't need the pass and id to be returned
class ShowUser(BaseModel):
    username: str
    email: str
    # Show all user blogs 
    blogs: List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body:str

    # Load the relationsip also, note that 'showBlog' using ShowUser so it should be below it 
    author: ShowUser
    class Config():
        orm_mode = True

    
class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
