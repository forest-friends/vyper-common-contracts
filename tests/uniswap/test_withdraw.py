def test_deposit_owner_only(stakable_uniswap_proxy, thomas, morpheus, ownable_exception_tester):
    ownable_exception_tester(
        stakable_uniswap_proxy.withdraw, thomas, {'from': morpheus})
