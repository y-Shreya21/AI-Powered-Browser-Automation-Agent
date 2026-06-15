from planner.models import Task


class Planner:

    def create_plan(
        self,
        goal: str
    ):

        goal = goal.lower()

        tasks = []

        if "job" in goal:

            tasks.append(
                Task(1, "open_linkedin")
            )

            tasks.append(
                Task(2, "search_jobs")
            )

            tasks.append(
                Task(3, "extract_results")
            )

        elif "research" in goal:

            tasks.append(
                Task(1, "open_google")
            )

            tasks.append(
                Task(2, "search_topic")
            )

            tasks.append(
                Task(3, "collect_information")
            )

        return tasks