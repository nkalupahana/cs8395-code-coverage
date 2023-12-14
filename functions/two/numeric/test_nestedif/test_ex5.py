from ..nestedif.ex5 import ex5

import pytest

def test_ex5():
    assert ex5(5, 3) == 2
    assert ex5(3, 5) == -2
    assert ex5(-5, 3) == -8
    assert ex5(3, -5) == 8
    assert ex5(-5, -3) == -2
    assert ex5(-3, -5) == 2
    assert ex5(0, 0) == 0
    assert ex5(0, 5) == 5
    assert ex5(5, 0) == 5
    assert ex5(0, -5) == -5
    assert ex5(-5, 0) == -5