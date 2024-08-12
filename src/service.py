import logging
from plugins.log import LoggerDependency
from plugins.session import SessionDataDependency
from nameko.rpc import rpc  # type: ignore
from .business.providers import GoogleProvider
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
]


class EdgeService:
    name = "edge_service"

    session_data: dict = SessionDataDependency()
    logger: logging.Logger = LoggerDependency()

    @rpc
    def generate_content(self, provider: str, model: MODEL, *args, **kwargs) -> str:
        match provider:
            case "OPENAI":
                ...
            case "ANTHROPIC":
                ...
            case "GOOGLE":
                response = GoogleProvider(model).generate_content(*args, **kwargs)
                text = response.text
            case _:
                text = ""
        return text

    @rpc
    def get_cost(self, provider):
        match provider:
            case _:
                ...
