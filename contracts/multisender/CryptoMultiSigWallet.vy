# @version ^0.2.0


# import interfaces.multisig.MultiSig as MultiSig


# implements: MultiSig


MAX_SIGNERS_COUNT: constant(uint256) = 5


signers: public(HashMap[bytes32, bool])


@external
def __init__(_signers: address[MAX_SIGNERS_COUNT]):
    for signer in _signers:
        if signer == ZERO_ADDRESS:
            continue

        signerHash: bytes32 = sha256(convert(signer, bytes32))
        self.signers[signerHash] = True


@view
@external
def isSigner(_account: address) -> bool: 
    return self.signers[sha256(convert(_account, bytes32))]