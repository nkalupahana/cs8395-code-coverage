from ..ifelseif.ex4 import ex4

import pytest

def test_ex4_even():
    assert ex4(10) == 20
    
def test_ex4_even2():
    assert ex4(2) == 12
    
def test_ex4_odd():
    assert ex4(5) == -5
    
def test_ex4_odd2():
    assert ex4(3) == 30
    
def test_ex4_odd3():
    assert ex4(1) == -9