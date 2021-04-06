from multicall import Call

POOCOIN = '0xB27ADAfFB9fEa1801459a1a81B17218288c097cc'


def from_wei(value):
    return value / 1e18


def test_call():
    call = Call(POOCOIN, 'name()(string)', [['name', None]])
    assert call() == {'name': 'PooCoin'}


def test_call_with_args():
    call = Call(POOCOIN, 'balanceOf(address)(uint256)', [['balance', from_wei]])
    assert isinstance(call([POOCOIN])['balance'], float)


def test_call_with_predefined_args():
    call = Call(POOCOIN, ['balanceOf(address)(uint256)', POOCOIN], [['balance', from_wei]])
    assert isinstance(call()['balance'], float)
