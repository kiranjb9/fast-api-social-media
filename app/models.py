from pydantic import EmailStr
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, text
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=True)
    content = Column(String, nullable=True)
    published = Column(Boolean, default=True)
    created = Column(TIMESTAMP(timezone=True), nullable=False, 
                     server_default=text('now()'))
    
    
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable = False)
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False,unique=True)
    password = Column(String, nullable=False)
    created = Column(TIMESTAMP(timezone=True), nullable=False, 
                     server_default=text('now()'))
    phone_number =Column(String)
    
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)

    

