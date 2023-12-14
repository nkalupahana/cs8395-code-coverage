from ..seqif.ex9 import ex9

import pytest

def test_positive():
    assert ex9(5) == 2

def test_negative():
    assert ex9(-2) == -8

def test_zero():
    assert ex9(0) == 0

def test_large_number():
    assert ex9(100) == 97

def test_negative_large_number():
    assert ex9(-100) == -400