from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication

# Create an instance of the FastAPI application
app = FastAPI()

# Generate database tables based on the models defined in the `models` module.
# The `create_all` method creates the tables in the database if they do not already exist.
# The `engine` is the connection to the database defined in the `database` module.
models.Base.metadata.create_all(engine)

# Include the `blog` router, which defines routes for blog-related endpoints.
app.include_router(blog.router)

# Include the `user` router, which defines routes for user-related endpoints.
app.include_router(user.router)

# Include the `authentication` router, which defines routes for authentication-related endpoints.
app.include_router(authentication.router)
