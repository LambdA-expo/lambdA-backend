"""
database configuration file
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    descriptipon: will create a new database session and sends it to the client and the session closes itself when the work is done. This function ensures each request has it’s independent database connections.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

