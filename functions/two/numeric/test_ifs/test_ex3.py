from ..ifs.ex3 import ex3

import pytest

# Test for when num1 is larger than num2
def test_ex3_larger():
    assert ex3(5, 3) == 2
    
# Test for when num2 is larger than num1
def test_ex3_smaller():
    assert ex3(3, 5) == 2
    
# Test for when num1 and num2 are equal
def test_ex3_equal():
    assert ex3(5, 5) == 0
    
# Test for negative numbers
def test_ex3_negative():
    assert ex3(-5, -3) == 2