from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import logging

load_dotenv(".env.dev")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


USE_IN_MEMORY_DB = os.getenv("USE_IN_MEMORY_DB", "0") == "1"

# if USE_IN_MEMORY_DB:
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
logger.info(f"Database URL: {DATABASE_URL}")
# else:
#     DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/auth_db")
#     engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()