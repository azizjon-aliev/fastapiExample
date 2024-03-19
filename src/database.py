from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.settings import settings


check_same_thread = not settings.database_url == "sqlite"

engine = create_engine(
    settings.database_url, connect_args={"check_same_thread": check_same_thread}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()