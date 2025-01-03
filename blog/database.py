from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Fixed the URL and removed the ":" before the database name
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# Creating the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Configuring the session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Creating the base class for models
Base = declarative_base()