# @version ^0.2.0


import interfaces.multisig.MultiSig as MultiSig


implements: MultiSig


MAX_SIGNERS_COUNT: constant(uint256) = 10


signers: public(address[MAX_SIGNERS_COUNT])
signersMap: public(HashMap[address, bool])


@external
def __init__(_signers: address[MAX_SIGNERS_COUNT]):
    for signer in _signers:
        self.signersMap[signer] = True


@view
@external
def isSigner(_account: address) -> bool: 
    return self.signersMap[_account]