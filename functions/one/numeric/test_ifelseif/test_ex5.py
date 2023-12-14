from ..ifelseif.ex5 import ex5

import pytest

def test_ex5_greater_than():
    assert ex5(10) == 15

def test_ex5_less_than():
    assert ex5(3) == -2

def test_ex5_equal():
    assert ex5(5) == 5

def test_ex5_negative():
    assert ex5(-10) == -15

def test_ex5_zero():
    assert ex5(0) == 0