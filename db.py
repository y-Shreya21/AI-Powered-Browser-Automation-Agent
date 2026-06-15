# setup_db.py

from storage.database import engine
from memory.models import Base

Base.metadata.create_all(engine)

print("Database created")