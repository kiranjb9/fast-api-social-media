from typing import List, Optional
from fastapi import  Depends, Response, status, HTTPException, APIRouter
from sqlalchemy import func

from sqlalchemy.orm import Session
from .. database import get_db
from .. import models, schemas, oauth2

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

# @router.get("/", response_model= List[schemas.PostOut])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db : Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user), 
              limit : int = 10, skip : int = 0, search : Optional[str] = ""):
    print(current_user)
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()


    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
            models.Post.id).filter(models.Post.title.contains(search)).limit(limit
            ).offset(skip).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model = schemas.Post)
def createposts(post : schemas.PostCreate, 
                db : Session = Depends(get_db), 
                current_user : int = Depends(oauth2.get_current_user)):
    
    print(current_user)
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return  new_post


@router.get("/latest_post", response_model=schemas.PostOut)
def get_latest_post(db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    # post = db.query(models.Post).order_by(models.Post.created.desc()).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
            models.Post.id).order_by(models.Post.created.desc()).first()
    print(print(current_user))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"No Post Present")
    
    return post
 
@router.get("/{id}",response_model=schemas.PostOut,)
def get_post(id : int, db : Session = Depends(get_db), 
             current_user : int = Depends(oauth2.get_current_user)):
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
            models.Post.id).filter(models.Post.id == id).first()
    print(print(current_user))
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Message" : f"Post with id {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id {id} not found")
    return  post


@router.delete("/{id}")
def deletePost(id : int, status_code = status.HTTP_204_NO_CONTENT, 
               db : Session = Depends(get_db),
               current_user : int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id) 
    print(print(post))

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id doesn't exists")

    if post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized to delete")
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Post,)
def update_post(id : int, post : schemas.PostCreate, db : Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post1 = post_query.first()

    if post1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id doesn't exists")
    
    if post1.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized to delete")
    
    post_query.update(post.dict(),synchronize_session=False)
    db.commit()
    
    return post_query.first()