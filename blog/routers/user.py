from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from blog import schema, database
from blog.repository import user

router = APIRouter(
    prefix="/user",
    tags=['users']
)
get_db = database.get_db

@router.post('/', response_model=schema.ShowUser)
def create(request: schema.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schema.ShowUser)
def get(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)
