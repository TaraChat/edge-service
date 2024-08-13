import anthropic
import os


class AnthropicProvider:

    def __init__(self, model_name: str):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_SECRET_KEY"))
        self.model_name = model_name

    def generate_content(self, prompt: str, **kwargs):
        response = self.client.messages.create(
            model=self.model_name,
            prompt=prompt,
            max_tokens=kwargs.get("max_tokens", 300),
            temperature=kwargs.get("temperature", 1),
            **kwargs
        )
        return response.content
