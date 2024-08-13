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

    @rpc
    def generate_content(self, provider: str, model: MODEL, *args, **kwargs) -> str:
        match provider.upper():
            case "OPENAI":
                response = OpenAIProvider(model).generate_content(*args, **kwargs)
                text = response  # Assuming the OpenAIProvider's generate_content method returns the generated text directly
            case "ANTHROPIC":
                response = AnthropicProvider(model).generate_content(*args, **kwargs)
                text = response  # Assuming the AnthropicProvider's generate_content method returns the generated text directly
            case "GOOGLE":
                response = GoogleProvider(model).generate_content(*args, **kwargs)
                text = (
                    response.text
                )  # Assuming the GoogleProvider's response has a `text` attribute
            case _:
                text = "Invalid provider specified."
        return text

    @rpc
    def stream_generate_content(self):
        yield
        pass

    @rpc
    def get_cost(self, provider):
        match provider:
            case _:
                ...
