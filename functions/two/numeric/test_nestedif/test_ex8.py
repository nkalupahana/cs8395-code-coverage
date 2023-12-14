from ..nestedif.ex8 import ex8

import pytest

# Test for when num1 > num2
def test_ex8_greater():
    assert ex8(5, 3) == 2

# Test for when num2 > num1
def test_ex8_less():
    assert ex8(3, 5) == 2

# Test for when num1 = num2
def test_ex8_equal():
    assert ex8(5, 5) == 0