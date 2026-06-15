from browser_use import Agent
from memory.memory_manager import MemoryManager

class BrowserAgent:
    def __init__(self):

        self.memory = MemoryManager()

    async def run(
        self,
        task,
        llm
    ):

        agent = Agent(
            task=task,
            llm=llm
        )

        result = await agent.run()
        observation = str(result.final_result() or result)[:300]
        self.memory.add_memory(
            goal=task,
            action=task,
            observation=observation
        )

        return result