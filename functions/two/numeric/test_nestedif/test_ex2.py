from ..nestedif.ex2 import ex2

import pytest

def test_ex2():
    assert ex2(5, 10) == 5

def test_ex2_negative():
    assert ex2(-10, -5) == 5

def test_ex2_large_difference():
    assert ex2(100, 10) == 900

def test_ex2_large_difference_negative():
    assert ex2(-100, -10) == 729

def test_ex2_equal_numbers():
    assert ex2(5, 5) == 0

def test_ex2_equal_numbers_negative():
    assert ex2(-5, -5) == 0