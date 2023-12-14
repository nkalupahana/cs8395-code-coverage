from ..none.ex8 import ex8

import pytest

# Test Case 1: num = 0
def test_ex8_1():
    assert ex8(0) == 3

# Test Case 2: num = 10
def test_ex8_2():
    assert ex8(10) == 13

# Test Case 3: num = -5
def test_ex8_3():
    assert ex8(-5) == -2

# Test Case 4: num = 2
def test_ex8_4():
    assert ex8(2) == 5

# Test Case 5: num = 100
def test_ex8_5():
    assert ex8(100) == 103

# Test Case 6: num = -10
def test_ex8_6():
    assert ex8(-10) == -7