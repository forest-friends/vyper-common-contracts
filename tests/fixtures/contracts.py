import pytest


@pytest.fixture(scope="module")
def stakable_uniswap_proxy(StakableProxy, deployer):
    yield StakableProxy.deploy({'from': deployer})
