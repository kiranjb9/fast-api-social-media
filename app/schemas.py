import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created : datetime

    class Config:
        arbitrary_types_allowed = True

class Post(PostBase):
    id : int
    created : datetime
    owner_id : int
    owner : UserOut

    class Config:
        arbitrary_types_allowed = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email : EmailStr
    password : str



class Userlogin(BaseModel):
    email : EmailStr
    password : str


class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str]

class vote(BaseModel):
    post_id : int
    dir : conint(le=1)