# agents/evaluator.py

class Evaluator:

    def evaluate(
        self,
        observation
    ):

        if observation["page_text"]:

            return True

        return False