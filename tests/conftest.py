import pytest
import brownie

pytest_plugins = [
    "fixtures.accounts",
    "fixtures.tokens",
    "fixtures.contracts",
    "fixtures.ownable",
    "fixtures.exception",
]


@pytest.fixture(scope="session")
def ZERO_ADDRESS():
    yield "0x0000000000000000000000000000000000000000"


@pytest.fixture(autouse=True)
def isolation_setup(module_isolation):
    pass
