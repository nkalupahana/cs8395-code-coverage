from ..ifs.ex9 import ex9

import pytest

def test_ex9():
    # Test case 1: x > y
    assert ex9(5, 3) == 2

    # Test case 2: x < y
    assert ex9(3, 5) == 2

    # Test case 3: x = y
    assert ex9(3, 3) == 0