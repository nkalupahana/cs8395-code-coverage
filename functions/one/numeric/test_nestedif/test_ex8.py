from ..nestedif.ex8 import ex8

import pytest

def test_ex8_equal():
    assert ex8(0) == 0

def test_ex8_greater_than():
    assert ex8(5) == 8

def test_ex8_greater_than_10():
    assert ex8(12) == 7

def test_ex8_less_than():
    assert ex8(-5) == -10

def test_ex8_less_than_negative_10():
    assert ex8(-15) == -12