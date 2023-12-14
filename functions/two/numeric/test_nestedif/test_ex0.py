from ..nestedif.ex0 import ex0

import pytest

def test_ex0():
    # Test case 1: both numbers are positive
    assert ex0(5, 3) == 8

    # Test case 2: num1 is negative and num2 is positive
    assert ex0(-5, 3) == -15

    # Test case 3: num1 is positive and num2 is negative
    assert ex0(5, -3) == 2

    # Test case 4: both numbers are negative
    assert ex0(-5, -3) == 1.6666666666666667