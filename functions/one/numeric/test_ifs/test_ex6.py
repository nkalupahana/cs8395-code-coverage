from ..ifs.ex6 import ex6

import pytest

def test_positive_number():
    assert ex6(5) == 25

def test_zero():
    assert ex6(0) == 0

def test_negative_number():
    assert ex6(-5) == 0

def test_large_number():
    assert ex6(100) == 500

def test_decimal_number():
    assert ex6(3.5) == 17.5