from ..ifs.ex4 import ex4

import pytest

def test_ex4_negative():
    assert ex4(-5) == 5

def test_ex4_positive():
    assert ex4(3) == 5

def test_ex4_zero():
    assert ex4(0) == 2