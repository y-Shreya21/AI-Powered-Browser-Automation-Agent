from planner.planner import Planner
from agents.agent import Agent
from browser.browser_manager import BrowserManager

goal = "Find AI jobs on LinkedIn"

planner = Planner()

plan = planner.create_plan(goal)

browser = BrowserManager()
browser.start()

agent = Agent()

agent.run(
    goal=goal,
    plan=plan,
    browser=browser
)

browser.stop()