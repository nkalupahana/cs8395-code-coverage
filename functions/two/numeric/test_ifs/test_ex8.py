from ..ifs.ex8 import ex8

import pytest

# Test for num1 > num2
def test_ex8_greater():
    assert ex8(5, 2) == 10

# Test for num1 <= num2
def test_ex8_less_equal():
    assert ex8(2, 5) == 7