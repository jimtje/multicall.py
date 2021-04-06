from multicall import Call, Multicall

POOCOIN = '0xB27ADAfFB9fEa1801459a1a81B17218288c097cc'


def from_wei(val):
    return val / 1e18


def from_ray(val):
    return val / 1e27


def test_multicall():
    multi = Multicall([
        Call(POOCOIN, 'totalSupply()(uint256)', [['supply', from_wei]]),
        Call(POOCOIN, ['balanceOf(address)(uint256)', POOCOIN], [['balance', from_ray]]),
    ])
    result = multi()
    assert isinstance(result['supply'], float)
    assert isinstance(result['balance'], float)
