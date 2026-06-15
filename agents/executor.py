# agents/executor.py

class Executor:

    def execute(
        self,
        task,
        browser
    ):

        if task.action == "open_linkedin":

            browser.goto(
                "https://linkedin.com"
            )

        elif task.action == "open_google":

            browser.goto(
                "https://google.com"
            )