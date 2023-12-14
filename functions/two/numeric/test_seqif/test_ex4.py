from ..seqif.ex4 import ex4

import pytest

def test_ex4_greater_than():
    assert ex4(5, 3) == 1

def test_ex4_less_than():
    assert ex4(3, 5) == 4

def test_ex4_positive_result():
    assert ex4(6, 2) == 2

def test_ex4_negative_result():
    assert ex4(-6, 2) == -4

def test_ex4_zero_result():
    assert ex4(0, 2) == 1