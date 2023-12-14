from ..none.ex4 import ex4

import pytest

def test_ex4():
    x = 5
    y = 3
    assert ex4(x, y) == 7
    
def test_ex4_zero():
    x = 0
    y = 0
    assert ex4(x, y) == 0
    
def test_ex4_negative():
    x = -5
    y = -3
    assert ex4(x, y) == -7
    
def test_ex4_decimal():
    x = 2.5
    y = 1.5
    assert ex4(x, y) == 4.5
    
def test_ex4_string():
    x = 'hello'
    y = 'world'
    with pytest.raises(TypeError):
        ex4(x, y)