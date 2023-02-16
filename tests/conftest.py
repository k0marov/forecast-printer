import pytest

from lib.core.config import Config


@pytest.fixture
def config():
    return Config()