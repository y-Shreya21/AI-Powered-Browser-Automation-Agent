# storage/database.py

from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///agent.db"

engine = create_engine(DATABASE_URL)