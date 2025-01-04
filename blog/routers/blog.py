from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from blog import schema, database, models
from typing import List
from blog.oauth2 import get_current_user
from blog.repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)
get_db = database.get_db


@router.get('/', response_model=List[schema.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.get('/{id}', status_code=200, response_model=schema.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    return blog.show(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schema.Blog, db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.Blog, db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    return blog.update(id, request, db)
