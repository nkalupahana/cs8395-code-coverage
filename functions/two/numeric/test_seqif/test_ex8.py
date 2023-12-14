from ..seqif.ex8 import ex8

import pytest

# Test case for when num1 is greater than num2
def test_ex8_greater():
    assert ex8(10, 5) == 225

# Test case for when num1 is less than num2
def test_ex8_less():
    assert ex8(5, 10) == -10

# Test case for when result is greater than 0
def test_ex8_result_greater():
    assert ex8(10, 5) == 225

# Test case for when result is less than 0
def test_ex8_result_less():
    assert ex8(5, 10) == -10