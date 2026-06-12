from datetime import datetime
from memory.models import MemoryEntry


class MemoryManager:

    def __init__(self):
        self.memories = []

    def add_memory(
        self,
        goal,
        action,
        observation
    ):
        memory = MemoryEntry(
            goal=goal,
            action=action,
            observation=observation,
            timestamp=datetime.now()
        )

        self.memories.append(memory)

    def get_memories(self):
        return self.memories