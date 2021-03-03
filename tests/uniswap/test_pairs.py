def test_add_pair_owner_only(stakable_uniswap_proxy, thomas, morpheus, ownable_exception_tester):
    ownable_exception_tester(
        stakable_uniswap_proxy.addUniswapPair, thomas, {'from': morpheus})
    ownable_exception_tester(
        stakable_uniswap_proxy.addUniswapPair, morpheus, {'from': thomas})


def test_remove_pair_owner_only(stakable_uniswap_proxy, thomas, morpheus, ownable_exception_tester):
    ownable_exception_tester(
        stakable_uniswap_proxy.removeUniswapPair, thomas, {'from': morpheus})
    ownable_exception_tester(
        stakable_uniswap_proxy.removeUniswapPair, morpheus, {'from': thomas})


def test_add_pairs(stakable_uniswap_proxy, deployer, thomas, morpheus, trinity, exception_tester, ZERO_ADDRESS):
    assert stakable_uniswap_proxy.lastPairIndex() == 0
    assert stakable_uniswap_proxy.indexByPair(thomas) == 0
    assert stakable_uniswap_proxy.indexByPair(morpheus) == 0
    assert stakable_uniswap_proxy.indexByPair(trinity) == 0
    assert stakable_uniswap_proxy.uniswapPairs(0) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(1) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(2) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(3) == ZERO_ADDRESS

    stakable_uniswap_proxy.addUniswapPair(thomas, {'from': deployer})
    assert stakable_uniswap_proxy.lastPairIndex() == 1
    assert stakable_uniswap_proxy.indexByPair(thomas) == 1
    assert stakable_uniswap_proxy.indexByPair(morpheus) == 0
    assert stakable_uniswap_proxy.indexByPair(trinity) == 0
    assert stakable_uniswap_proxy.uniswapPairs(0) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(1) == thomas
    assert stakable_uniswap_proxy.uniswapPairs(2) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(3) == ZERO_ADDRESS

    exception_tester("pair is exist", stakable_uniswap_proxy.addUniswapPair,
                     thomas, {'from': deployer})
    exception_tester("", stakable_uniswap_proxy.addUniswapPair,
                     ZERO_ADDRESS, {'from': deployer})

    stakable_uniswap_proxy.removeUniswapPair(thomas, {'from': deployer})
    assert stakable_uniswap_proxy.lastPairIndex() == 0
    assert stakable_uniswap_proxy.indexByPair(thomas) == 0
    assert stakable_uniswap_proxy.indexByPair(morpheus) == 0
    assert stakable_uniswap_proxy.indexByPair(trinity) == 0
    assert stakable_uniswap_proxy.uniswapPairs(0) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(1) == thomas
    assert stakable_uniswap_proxy.uniswapPairs(2) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(3) == ZERO_ADDRESS

    stakable_uniswap_proxy.addUniswapPair(trinity, {'from': deployer})
    assert stakable_uniswap_proxy.lastPairIndex() == 1
    assert stakable_uniswap_proxy.indexByPair(thomas) == 0
    assert stakable_uniswap_proxy.indexByPair(morpheus) == 0
    assert stakable_uniswap_proxy.indexByPair(trinity) == 1
    assert stakable_uniswap_proxy.uniswapPairs(0) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(1) == trinity
    assert stakable_uniswap_proxy.uniswapPairs(2) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(3) == ZERO_ADDRESS

    stakable_uniswap_proxy.addUniswapPair(thomas, {'from': deployer})
    assert stakable_uniswap_proxy.lastPairIndex() == 2
    assert stakable_uniswap_proxy.indexByPair(thomas) == 2
    assert stakable_uniswap_proxy.indexByPair(morpheus) == 0
    assert stakable_uniswap_proxy.indexByPair(trinity) == 1
    assert stakable_uniswap_proxy.uniswapPairs(0) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(1) == trinity
    assert stakable_uniswap_proxy.uniswapPairs(2) == thomas
    assert stakable_uniswap_proxy.uniswapPairs(3) == ZERO_ADDRESS

    stakable_uniswap_proxy.addUniswapPair(morpheus, {'from': deployer})
    assert stakable_uniswap_proxy.lastPairIndex() == 3
    assert stakable_uniswap_proxy.indexByPair(thomas) == 2
    assert stakable_uniswap_proxy.indexByPair(morpheus) == 3
    assert stakable_uniswap_proxy.indexByPair(trinity) == 1
    assert stakable_uniswap_proxy.uniswapPairs(0) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(1) == trinity
    assert stakable_uniswap_proxy.uniswapPairs(2) == thomas
    assert stakable_uniswap_proxy.uniswapPairs(3) == morpheus

    stakable_uniswap_proxy.removeUniswapPair(thomas, {'from': deployer})
    assert stakable_uniswap_proxy.lastPairIndex() == 2
    assert stakable_uniswap_proxy.indexByPair(thomas) == 0
    assert stakable_uniswap_proxy.indexByPair(morpheus) == 2
    assert stakable_uniswap_proxy.indexByPair(trinity) == 1
    assert stakable_uniswap_proxy.uniswapPairs(0) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(1) == trinity
    assert stakable_uniswap_proxy.uniswapPairs(2) == morpheus
    assert stakable_uniswap_proxy.uniswapPairs(3) == morpheus

    stakable_uniswap_proxy.removeUniswapPair(morpheus, {'from': deployer})
    assert stakable_uniswap_proxy.lastPairIndex() == 1
    assert stakable_uniswap_proxy.indexByPair(thomas) == 0
    assert stakable_uniswap_proxy.indexByPair(morpheus) == 0
    assert stakable_uniswap_proxy.indexByPair(trinity) == 1
    assert stakable_uniswap_proxy.uniswapPairs(0) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(1) == trinity
    assert stakable_uniswap_proxy.uniswapPairs(2) == morpheus
    assert stakable_uniswap_proxy.uniswapPairs(3) == morpheus

    exception_tester("pair is not exist",
                     stakable_uniswap_proxy.removeUniswapPair, morpheus, {'from': deployer})

    stakable_uniswap_proxy.removeUniswapPair(trinity, {'from': deployer})
    assert stakable_uniswap_proxy.lastPairIndex() == 0
    assert stakable_uniswap_proxy.indexByPair(thomas) == 0
    assert stakable_uniswap_proxy.indexByPair(morpheus) == 0
    assert stakable_uniswap_proxy.indexByPair(trinity) == 0
    assert stakable_uniswap_proxy.uniswapPairs(0) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(1) == trinity
    assert stakable_uniswap_proxy.uniswapPairs(2) == morpheus
    assert stakable_uniswap_proxy.uniswapPairs(3) == morpheus

    stakable_uniswap_proxy.addUniswapPair(thomas, {'from': deployer})
    assert stakable_uniswap_proxy.lastPairIndex() == 1
    assert stakable_uniswap_proxy.indexByPair(thomas) == 1
    assert stakable_uniswap_proxy.indexByPair(morpheus) == 0
    assert stakable_uniswap_proxy.indexByPair(trinity) == 0
    assert stakable_uniswap_proxy.uniswapPairs(0) == ZERO_ADDRESS
    assert stakable_uniswap_proxy.uniswapPairs(1) == thomas
    assert stakable_uniswap_proxy.uniswapPairs(2) == morpheus
    assert stakable_uniswap_proxy.uniswapPairs(3) == morpheus
