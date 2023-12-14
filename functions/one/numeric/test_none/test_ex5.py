from ..none.ex5 import ex5

import pytest

def test_ex5():
    assert ex5(5) == 8
    assert ex5(10) == 13
    assert ex5(0) == 3
    assert ex5(-5) == 0
    assert ex5(2.5) == 5.5
    assert ex5(-10.5) == -7.5