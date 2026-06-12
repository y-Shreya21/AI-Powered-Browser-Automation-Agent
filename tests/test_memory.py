# tests/test_memory.py

from memory.memory_manger import MemoryManager

memory = MemoryManager()

memory.add_memory(
    goal="Search AI jobs",
    action="Opened LinkedIn",
    observation="Found 120 jobs"
)

for item in memory.get_memories():
    print(item)