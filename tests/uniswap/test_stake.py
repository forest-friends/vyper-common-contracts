def test_deposit_owner_only(stakable_uniswap_proxy, morpheus, ownable_exception_tester):
    ownable_exception_tester(
        stakable_uniswap_proxy.stake, 1, {'from': morpheus})
