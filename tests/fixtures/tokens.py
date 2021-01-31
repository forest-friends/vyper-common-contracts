import pytest


ERC20_TOKEN_NAME = "Test token"
ERC20_TOKEN_SYMBOL = "TEST"
ERC20_TOKEN_DECIMALS = 18
ERC20_TOKEN_INITIAL_SUPPLY = 1_000_000


@pytest.fixture(scope="module")
def erc20_token(ERC20Basic, neo):
    yield ERC20Basic.deploy(ERC20_TOKEN_NAME, ERC20_TOKEN_SYMBOL, ERC20_TOKEN_DECIMALS, ERC20_TOKEN_INITIAL_SUPPLY, {'from': neo})
