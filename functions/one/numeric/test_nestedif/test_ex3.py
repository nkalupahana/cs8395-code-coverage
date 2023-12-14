from ..nestedif.ex3 import ex3

import pytest

def test_ex3_positive():
    assert ex3(5) == 10

def test_ex3_negative():
    assert ex3(-5) == -5
    
def test_ex3_zero():
    assert ex3(0) == 0
    
def test_ex3_greater_than_10():
    assert ex3(6) == 12
    assert ex3(11) == 16
    
def test_ex3_less_than_10():
    assert ex3(3) == 6
    assert ex3(9) == 9