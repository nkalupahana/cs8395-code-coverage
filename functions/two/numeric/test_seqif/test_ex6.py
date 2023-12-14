from ..seqif.ex6 import ex6

import pytest

# Test case for when num1 is greater than num2
def test_ex6_greater():
    assert ex6(10, 5) == 5

# Test case for when num2 is greater than num1
def test_ex6_less():
    assert ex6(5, 10) == 5

# Test case for when result is greater than 5
def test_ex6_result():
    assert ex6(10, 5) == 10

# Test case for when result is less than or equal to 5
def test_ex6_less_result():
    assert ex6(5, 10) == 5