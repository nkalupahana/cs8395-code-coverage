from ..ifelseif.ex2 import ex2

import pytest

def test_ex2_negative():
    assert ex2(-5) == 5

def test_ex2_single_digit():
    assert ex2(5) == 50

def test_ex2_large_number():
    assert ex2(100) == 50

def test_ex2_zero():
    assert ex2(0) == 0

def test_ex2_negative_float():
    assert ex2(-3.5) == 3.5

def test_ex2_positive_float():
    assert ex2(2.5) == 25