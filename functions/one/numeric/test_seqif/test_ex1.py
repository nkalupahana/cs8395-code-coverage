from ..seqif.ex1 import ex1

import pytest

def test_ex1_greater_than_5():
    assert ex1(6) == 11
    
def test_ex1_less_than_or_equal_to_5():
    assert ex1(3) == -2
    
def test_ex1_equal_to_0():
    assert ex1(0) == 10
    
def test_ex1_negative_number():
    assert ex1(-5) == -10