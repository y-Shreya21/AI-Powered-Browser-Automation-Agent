# services/llm_services.py

from ollama import chat


class LLMService:

    def ask(self, prompt: str):

        response = chat(
            model="qwen3:8b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content
