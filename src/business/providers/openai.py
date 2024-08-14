import openai


class OpenAIProvider:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_text(self, prompt, model, max_tokens=50):
        response = openai.Completion.create(
            engine=model, prompt=prompt, max_tokens=max_tokens
        )
        return response.choices[0].text.strip()

    def stream_autocomplete(self, prompt, model):
        completion = openai.Completion.create(
            engine=model, prompt=prompt, max_tokens=50, stream=True
        )
        for message in completion:
            if "choices" in message:
                yield message["choices"][0]["text"]
