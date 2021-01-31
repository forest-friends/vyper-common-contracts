#!/usr/bin/python3

import brownie
import pytest
from brownie.test import given, strategy


@given(amount=strategy('uint256', min_value=1, max_value=10**3))
def test_vote_simple(neo, morpheus, amount):
    print(amount)