# @version ^0.2.0


# import interfaces.multisig.MultiSig as MultiSig


# implements: MultiSig


MAX_SIGNERS_COUNT: constant(uint256) = 5


signers: public(HashMap[address, bool])


@external
def __init__(_signers: address[MAX_SIGNERS_COUNT]):
    for signer in _signers:
        if signer == ZERO_ADDRESS:
            continue
        self.signers[signer] = True


@view
@external
def isSigner(_account: address) -> bool: 
    return self.signers[_account]