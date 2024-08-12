import logging
from plugins.log import LoggerDependency
from plugins.session import SessionDataDependency
from nameko.rpc import rpc  # type: ignore


class EdgeService:
    name = "edge_service"

    session_data: dict = SessionDataDependency()
    logger: logging.Logger = LoggerDependency()

    @rpc
    def sample_method(self, payload):
        """Returns the payload received."""
        return payload
