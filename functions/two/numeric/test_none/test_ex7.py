from ..none.ex7 import ex7

import pytest

def test_ex7():
    assert ex7(3, 4) == 4

def test_ex7_negative():
    assert ex7(-5, 10) == 10

def test_ex7_zero():
    assert ex7(0, 5) == 5

def test_ex7_decimal():
    assert ex7(3.5, 2.5) == 2.5

def test_ex7_string():
    assert ex7("hello", "world") == "world"