from ..ifs.ex2 import ex2

def test_ex2_positive():
    assert ex2(5) == 10

def test_ex2_negative():
    assert ex2(-5) == -10

def test_ex2_zero():
    assert ex2(0) == -5