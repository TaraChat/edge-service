import pytest
from nameko.standalone.rpc import ClusterRpcProxy
from src.config import config

config = {"AMQP_URI": config}


def test_envvars():
    assert config["AMQP_URI"] is not None


def test_simple_rpc_call():
    payload = "test"
    with ClusterRpcProxy(config) as rpc:
        response = rpc.edge_service.sample_method(payload)
    assert response == payload, "Microservice not working as expected..."


if __name__ == "__main__":
    pytest.main()
