from sqlalchemy.orm import Session
from .. import models, schema  # Import models (DB schema) and schema (Pydantic models)
from fastapi import HTTPException, status  # Import HTTPException and status for error handling


# Function to get all blogs from the database
def get_all(db: Session):
    # Query the 'Blog' table and return all blog entries
    blogs = db.query(models.Blog).all()
    return blogs


# Function to create a new blog in the database
def create(request: schema.Blog, db: Session):
    # Create a new Blog object using data from the request
    new_blog = models.Blog(title=request.title, body=request.body,
                           user_id=1)  # user_id=1 is hardcoded (to be changed for real authentication)
    # Add the new blog to the session
    db.add(new_blog)
    # Commit the transaction to save the new blog to the database
    db.commit()
    # Refresh the session to get the updated object with its assigned ID
    db.refresh(new_blog)
    return new_blog  # Return the created blog


# Function to delete a blog from the database by its ID
def destroy(id: int, db: Session):
    # Query the 'Blog' table for the blog with the given ID
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    # If no blog is found, raise a 404 error
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    else:
        # If the blog is found, delete it
        blog.delete(synchronize_session=False)  # 'synchronize_session=False' is used to avoid unnecessary syncing
        db.commit()  # Commit the transaction to delete the blog
    return 'done'  # Return a success message


# Function to update an existing blog's details
def update(id: int, request: schema.Blog, db: Session):
    # Query the 'Blog' table for the blog with the given ID
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    # If no blog is found, raise a 404 error
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Found')
    else:
        # If the blog is found, update it with the new data from the request
        blog.update(request.dict())  # Using .dict() to convert the Pydantic model to a dictionary
        db.commit()  # Commit the transaction to save the changes
    return 'updated'  # Return a success message


# Function to get a specific blog by its ID
def show(id: int, db: Session):
    # Query the 'Blog' table for the blog with the given ID
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # If no blog is found, raise a 404 error with a custom message
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    return blog  # Return the found blog
