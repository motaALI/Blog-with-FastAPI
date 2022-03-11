from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from blog.database import Base

#Create a relationships
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'

    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    # published = Column(Boolean)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    blogs = relationship("Blog", back_populates="author")