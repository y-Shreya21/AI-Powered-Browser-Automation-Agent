from browser_use import Agent


class BrowserUseAgent:

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

        return result