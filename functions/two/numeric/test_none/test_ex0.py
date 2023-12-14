from ..none.ex0 import ex0

import pytest

def test_ex0():
    assert ex0(10, 5) == 5
    
def test_ex0_negative():
    assert ex0(-10, -5) == -5
    
def test_ex0_zero():
    assert ex0(0, 0) == 0
    
def test_ex0_float():
    assert ex0(10.5, 5.2) == 5.3
    
def test_ex0_large_numbers():
    assert ex0(1000000000000, 999999999999) == 1
    
def test_ex0_decimals():
    assert ex0(0.5, 0.2) == 0.3