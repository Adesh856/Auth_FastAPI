from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv
import os
load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")



# Define the database URL
SQLALCHEMY_DATABASE_URL = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

print(SQLALCHEMY_DATABASE_URL,"================>")
#Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)


#Create a sessionmaker object to manage database sessions.
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

#Create a declarative base for database models
Base = declarative_base()



#Dependency
def get_db():
    """
    Get a database session. 
    """
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()  