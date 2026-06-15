from datetime import datetime

from sqlalchemy.orm import Session

from memory.models import Memory
from storage.database import engine


class MemoryManager:

    def __init__(self):
        self.memories = []

    def add_memory(
        self,
        goal,
        action,
        observation
    ):
        memory = Memory(
            goal=goal,
            action=action,
            observation=observation,
            timestamp=datetime.now()
        )

        with Session(engine) as session:
            session.add(memory)
            session.commit()
