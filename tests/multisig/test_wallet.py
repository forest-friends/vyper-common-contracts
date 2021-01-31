#!/usr/bin/python3

import brownie
import pytest
from brownie.test import given, strategy


def test_(ZERO_ADDRESS, multisig_wallet, erc20_token, neo, morpheus, trinity):
    erc20_token.transfer(multisig_wallet, 1_000, {'from': neo})

    assert multisig_wallet.isSigner(neo, {'from': neo}) == True
    assert multisig_wallet.isSigner(morpheus, {'from': morpheus}) == True
    assert multisig_wallet.isSigner(trinity, {'from': trinity}) == True

    assert erc20_token.balanceOf(multisig_wallet) == 1_000
