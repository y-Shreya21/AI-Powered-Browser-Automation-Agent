# tests/test_planner.py

from planner.planner import Planner

planner = Planner()

plan = planner.create_plan("Find AI jobs on LinkedIn")

print(plan)