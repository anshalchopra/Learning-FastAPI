from blog.hashing import Hash  # Importing the Hashing utility to hash passwords
from blog import models, schema  # Importing models (DB schema) and schema (Pydantic models)
from sqlalchemy.orm import Session  # Importing SQLAlchemy's Session class for DB interactions
from fastapi import Depends, HTTPException, \
    status  # Importing FastAPI utilities for dependency injection and error handling


# Function to create a new user in the database
def create(request: schema.User, db: Session):
    # Hash the password using bcrypt before saving it to the database
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    # Add the new user to the session
    db.add(new_user)
    # Commit the transaction to save the new user to the database
    db.commit()
    # Refresh the session to retrieve the updated user object with its assigned ID
    db.refresh(new_user)
    # Return the request data (to be consistent with the response model)
    return request


# Function to get a user by their ID from the database
def get(id: int, db: Session):
    # Query the 'User' table to find the user with the specified ID
    user = db.query(models.User).filter(models.User.id == id).first()
    # If the user is not found, raise a 404 error with a custom message
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    # Return the user object if found
    return user
