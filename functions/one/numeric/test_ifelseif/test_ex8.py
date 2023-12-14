from ..ifelseif.ex8 import ex8

import pytest

def test_ex8_positive():
    assert ex8(10) == 20

def test_ex8_negative():
    assert ex8(-10) == -20

def test_ex8_zero():
    assert ex8(0) == 0