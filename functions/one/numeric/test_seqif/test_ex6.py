from ..seqif.ex6 import ex6

import pytest

def test_ex6_positive():
    assert ex6(10) == 33

def test_ex6_negative():
    assert ex6(-5) == -4

def test_ex6_zero():
    assert ex6(0) == 1

def test_ex6_odd():
    assert ex6(3) == 4

def test_ex6_even():
    assert ex6(4) == 12