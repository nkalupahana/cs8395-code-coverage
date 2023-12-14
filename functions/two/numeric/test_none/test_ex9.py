from ..none.ex9 import ex9

import pytest

def test_ex9():
    assert ex9(5, 3) == 2
    assert ex9(0, 0) == 0
    assert ex9(-5, 2) == -7
    assert ex9(10, -5) == 15
    assert ex9(2.5, 1.5) == 1
    assert ex9(1000000, 500000) == 500000
    assert ex9(-10, -20) == 10
    assert ex9(3, -3) == 6
    assert ex9(0, 5) == -5
    assert ex9(7, 7) == 0