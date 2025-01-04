from pydantic import BaseModel
from typing import List, Optional


# Base class for the Blog schema (used for both creating and updating Blog objects)
class BlogBase(BaseModel):
    title: str  # Title of the blog
    body: str  # Content of the blog


# Blog schema for returning data (inherits from BlogBase and sets orm_mode to True)
class Blog(BlogBase):
    class Config():
        orm_mode = True  # Tells Pydantic to treat ORM models as dict-like objects


# User schema for creating and returning user data
class User(BaseModel):
    name: str  # User's name
    email: str  # User's email (usually unique)
    password: str  # User's password (hashed before storage)


# Schema for displaying user information, including a list of associated blogs
class ShowUser(BaseModel):
    name: str  # User's name
    email: str  # User's email
    blogs: List[Blog] = None  # List of blogs created by the user, defaults to None if no blogs exist

    # Ensures that the ORM model (SQLAlchemy) can be converted to this Pydantic model
    class Config():
        orm_mode = True


# Schema for displaying blog information with its creator (User)
class ShowBlog(BaseModel):
    title: str  # Title of the blog
    body: str  # Content of the blog
    creator: ShowUser  # Information about the creator (user) of the blog

    class Config():
        orm_mode = True  # Ensures that ORM models can be converted to this Pydantic model


# Schema for user login (only username and password required)
class Login(BaseModel):
    username: str  # Username used for login (often the email)
    password: str  # Password for authentication


# Token schema to return an access token and its type (e.g., Bearer)
class Token(BaseModel):
    access_token: str  # The JWT token that is used for authentication
    token_type: str  # The type of token, typically "bearer"


# TokenData schema to store token-related data (optional email field for the decoded token)
class TokenData(BaseModel):
    email: Optional[str] = None  # Email of the user embedded in the token (optional, can be None)
