from ..nestedif.ex1 import ex1

import pytest

def test_ex1_positive():
    assert ex1(3) == 2

def test_ex1_zero():
    assert ex1(0) == 0

def test_ex1_negative():
    assert ex1(-2) == -2

def test_ex1_greater_than_5():
    assert ex1(7) == 14

def test_ex1_equal_to_5():
    assert ex1(5) == 4

def test_ex1_less_than_5():
    assert ex1(2) == 1

def test_ex1_float():
    assert ex1(2.5) == 1.5

def test_ex1_string():
    with pytest.raises(TypeError):
        ex1("test")