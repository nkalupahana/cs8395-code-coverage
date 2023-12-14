from ..seqif.ex2 import ex2

import pytest

# Test cases for positive numbers
def test_ex2_positive():
    assert ex2(4) == 2
    assert ex2(10) == 8
    assert ex2(100) == 98

# Test cases for negative numbers
def test_ex2_negative():
    assert ex2(-2) == -7
    assert ex2(-10) == -15
    assert ex2(-100) == -105

# Test case for zero
def test_ex2_zero():
    assert ex2(0) == 0