from blog.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


# Define the User model, which represents the 'user' table in the database.
class User(Base):
    # Specify the name of the database table.
    __tablename__ = 'user'

    # Define the table's columns.
    id = Column(Integer, primary_key=True, index=True)  # Primary key column for user ID.
    name = Column(String)  # Column to store the user's name.
    email = Column(String)  # Column to store the user's email address.
    password = Column(String)  # Column to store the hashed password.

    # Define a relationship with the Blog model.
    # This allows you to access the blogs associated with a user.
    # `back_populates` links this relationship to the `creator` field in the Blog model.
    blogs = relationship("Blog", back_populates="creator")


# Define the Blog model, which represents the 'blogs' table in the database.
class Blog(Base):
    # Specify the name of the database table.
    __tablename__ = 'blogs'

    # Define the table's columns.
    id = Column(Integer, primary_key=True, index=True)  # Primary key column for blog ID.
    title = Column(String)  # Column to store the blog's title.
    body = Column(String)  # Column to store the blog's content.
    user_id = Column(Integer, ForeignKey('user.id'))  # Foreign key referencing the User table.

    # Define a relationship with the User model.
    # This allows you to access the user who created the blog.
    # `back_populates` links this relationship to the `blogs` field in the User model.
    creator = relationship("User", back_populates="blogs")
