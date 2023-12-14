from ..ifs.ex7 import ex7

import pytest

def test_ex7_positive():
    assert ex7(5) == 10

def test_ex7_zero():
    assert ex7(0) == 1

def test_ex7_negative():
    assert ex7(-5) == -4