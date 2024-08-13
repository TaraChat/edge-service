from openai import OpenAI
import os


class OpenAIProvider:

    def __init__(self, model_name: str):
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        self.model_name = model_name

    def generate_content(self, prompt: str, **kwargs):
        response = self.client.chat.completions.create(
            model=self.model_name,
            prompt=prompt,
            max_tokens=kwargs.get("max_tokens", 300),
            temperature=kwargs.get("temperature", 1),
            **kwargs
        )
        return response.choices[0].text.strip()
