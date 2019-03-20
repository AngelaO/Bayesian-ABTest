# file: algebra/tests/test_add.py
import algebra

def test_add_positive():
    res = algebra.add(2, 2)
    assert isintance(res, int)
    assert res == 4

def test_add_negative():
    res = algebra.add(2, -3)
    assert isinstance(res, int)
    assert res == -1