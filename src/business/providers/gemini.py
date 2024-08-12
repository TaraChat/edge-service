import google.generativeai as genai
import os


genai.configure(api_key=os.environ["GEMINI_SECRET_KEY"])


class GeminiProvider:

    def __init__(self, model_name: str):
        self.model = genai.GenerativeModel(model_name=model_name)

    def generate_content(self, *args, **kwargs):
        return self.model.generate_content(*args, **kwargs)
