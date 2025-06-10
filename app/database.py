import sqlalchemy as db
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base

# fetch database url from .env file
load_dotenv()
url = os.getenv("DATABASEURL")

# object which creates connection to the database
engine = db.create_engine(url)

# sessions provide a query interface to retrieve objects from the database, autocommit and autoflush set to false means permanent commitments will not be made to database unless specified
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_table():
    Base.metadata.create_all(bind=engine)
