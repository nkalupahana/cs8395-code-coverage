from ..ifs.ex0 import ex0

import pytest

def test_ex0():
    # Test case 1: arg1 > arg2
    assert ex0(10, 5) == 110

    # Test case 2: arg1 < arg2
    assert ex0(5, 10) == 105

    # Test case 3: arg1 == arg2
    assert ex0(10, 10) == 200