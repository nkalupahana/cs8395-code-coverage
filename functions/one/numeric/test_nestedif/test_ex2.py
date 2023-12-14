from ..nestedif.ex2 import ex2

import pytest

def test_ex2_positive_even():
    assert ex2(4) == 8

def test_ex2_positive_odd():
    assert ex2(5) == 6

def test_ex2_zero():
    assert ex2(0) == -1

def test_ex2_negative():
    assert ex2(-6) == -7