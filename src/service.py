import logging
from plugins.log import LoggerDependency
from plugins.session import SessionDataDependency
from nameko.rpc import rpc  # type: ignore
from .business.providers import GoogleProvider, OpenAIProvider, AnthropicProvider
from typing import Literal


PROVIDER = Literal[
    "GOOGLE",
    "OPENAI",
    "ANTHROPIC",
]

MODEL = Literal[
    # Google
    "gemini-1.5-flash",  # In (Audio, images, videos, and text)
    "gemini-1.5-pro",  # In (Audio, images, videos, and text)
    "gemini-1.0-pro",  # In Text
    "text-embedding-004",  # In Text
    "aqa",  # In Text
    # Anthropic
    "claude-2",  # Example model name for Anthropic
    "claude-instant-1",  # Another example model name for Anthropic
    "claude-3-opus-20240229",
    # OpenAI
    "text-davinci-003",  # In Text
    "text-davinci-002",  # In Text
    "gpt-3.5-turbo",  # In Text
    "gpt-4",  # In Text
    "davinci",  # In Text
    "curie",  # In Text
    "babbage",  # In Text
    "ada",  # In Text
    # Add other models here as needed for additional providers
]


class EdgeService:
    name = "edge_service"

    session_data: dict = SessionDataDependency()
    logger: logging.Logger = LoggerDependency()

    def __init__(self):
        self.providers = {
            "OPENAI": OpenAIProvider(api_key="your-openai-api-key"),
            "ANTHROPIC": AnthropicProvider(api_key="your-anthropic-api-key"),
            "GOOGLE": GoogleProvider(api_key="your-google-api-key"),
        }

    @rpc
    def generate_text(self, provider: str, model: MODEL, *args, **kwargs) -> str:
        provider_instance = self.providers.get(provider)
        if provider_instance:
            return provider_instance.generate_text(model, *args, **kwargs)
        else:
            return {"error": "Invalid provider"}

    @rpc
    def stream_autocomplete(self, provider, model, prompt):
        provider_instance = self.providers.get(provider)
        if provider_instance:
            return list(provider_instance.stream_autocomplete(prompt, model))
        else:
            return {"error": "Invalid provider"}

    @rpc
    def get_cost(self, provider):
        match provider:
            case _:
                ...
