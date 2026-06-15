from services.llm_service import LLMService

llm = LLMService()

response = llm.ask(
    "Create a browser automation plan to find AI jobs on LinkedIn"
)

print(response)