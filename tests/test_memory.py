# tests/test_memory.py

from sqlalchemy.orm import Session

from memory.memory_manager import MemoryManager
from memory.models import Memory
from storage.database import engine

memory = MemoryManager()

memory.add_memory(
    goal="Search AI jobs",
    action="Opened LinkedIn",
    observation="Found 120 jobs"
)

with Session(engine) as session:
    memories = session.query(Memory).all()
    for memory in memories:
        print(memory)