from dataclasses import dataclass
from datetime import datetime


@dataclass
class MemoryEntry:
    goal: str
    action: str
    observation: str
    timestamp: datetime