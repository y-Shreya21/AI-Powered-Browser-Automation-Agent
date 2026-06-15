# agents/observer.py

class Observer:

    def observe(
        self,
        browser,
        memory,
        goal,
        action
    ):

        text = browser.extract_text()

        memory.add_memory(
            goal=goal,
            action=action,
            observation=text[:300]
        )

        return {
            "page_text": text[:1000]
        }