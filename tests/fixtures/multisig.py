import pytest


@pytest.fixture(scope="module")
def multisig_wallet(MultiSigWallet, neo, morpheus, trinity, ZERO_ADDRESS):
    yield MultiSigWallet.deploy(
        [neo, morpheus, trinity, ZERO_ADDRESS, ZERO_ADDRESS], {'from': neo})
