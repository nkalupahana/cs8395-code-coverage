from ..seqif.ex8 import ex8

import pytest

def test_ex8_positive():
    assert ex8(10) == 30
    assert ex8(100) == 210

def test_ex8_negative():
    assert ex8(-10) == -15
    assert ex8(-100) == -105