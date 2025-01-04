from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database URL for SQLite. The URL format for SQLite is 'sqlite:///relative/path/to/db'.
# Here, 'blog.db' is the database file located in the current directory.
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# Create a database engine using SQLAlchemy. The engine is responsible for managing the database connection.
# The `connect_args` parameter is used to set SQLite-specific options.
# `check_same_thread=False` is required for SQLite when using it with multiple threads (e.g., in web apps).
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Configure the sessionmaker to handle database sessions.
# `autocommit=False` ensures transactions are explicitly committed.
# `autoflush=False` prevents automatic flushing of changes to the database before queries are executed.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create a declarative base class that is used to define models (tables) in the database.
# Models will inherit from this base class to map Python objects to database tables.
Base = declarative_base()


# Dependency function to get a database session.
# This function is used with FastAPI's dependency injection system to provide a session for each request.
def get_db():
    # Create a new database session.
    db = SessionLocal()
    try:
        # Yield the session to be used in the request.
        yield db
    finally:
        # Ensure the database session is closed after the request is handled.
        db.close()
