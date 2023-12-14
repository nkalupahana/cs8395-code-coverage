from ..none.ex9 import ex9

import pytest

def test_ex9():
    assert ex9(5) == 10

def test_ex9_negative():
    assert ex9(-5) == 0

def test_ex9_zero():
    assert ex9(0) == 5

def test_ex9_decimal():
    assert ex9(2.5) == 7.5

def test_ex9_string():
    with pytest.raises(TypeError):
        ex9("5")