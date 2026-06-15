# agents/agent.py

from agents.executor import Executor
from agents.observer import Observer
from agents.evaluator import Evaluator
from memory.memory_manager import MemoryManager

class Agent:

    def __init__(self):

        self.executor = Executor()

        self.observer = Observer()

        self.evaluator = Evaluator()

        self.memory = MemoryManager()

    def run(
        self,
        goal,
        plan,
        browser
    ):

        for task in plan:

            self.executor.execute(
                task,
                browser
            )

            observation = (
                self.observer.observe(
                    browser,
                    self.memory,
                    goal,
                    task.action
                )
            )

            success = (
                self.evaluator.evaluate(
                    observation
                )
            )

            print(
                task.action,
                success
            )