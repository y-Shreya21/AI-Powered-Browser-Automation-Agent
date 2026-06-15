import asyncio

from agents.browser_use_agent import (
    BrowserUseAgent
)

from services.ollama_provider import (
    get_llm
)


async def main():

    llm = get_llm()

    agent = BrowserUseAgent()

    result = await agent.run(
        """
        Open Google.

        Search for:
        AI Engineer Jobs

        Summarize findings.
        """,
        llm
    )

    print(result)


asyncio.run(main())