from ..nestedif.ex5 import ex5

import pytest

def test_ex5_positive():
    assert ex5(5) == 20

def test_ex5_zero():
    assert ex5(0) == 0

def test_ex5_negative():
    assert ex5(-5) == -5