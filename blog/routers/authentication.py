from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog import schema, database, models
from blog.hashing import Hash
from datetime import timedelta
from blog.token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from typing import Annotated
from blog.schema import Token

router = APIRouter(
    tags = ['authentication']
)

@router.post('/login')
def login(request:Annotated[OAuth2PasswordRequestForm, Depends()], db:Session = Depends(database.get_db)) -> Token:
    print(f"Received login request with username: {request.username}")  # Print statement
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Invalid Credentials')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect Password')
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return Token(access_token = access_token, token_type ='bearer')