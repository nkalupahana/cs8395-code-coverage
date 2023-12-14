from ..none.ex2 import ex2

import pytest

def test_ex2():
    assert ex2(3, 5) == 5
    assert ex2(0, 0) == 0
    assert ex2(-1, 1) == 0
    assert ex2(5, -2) == 3
    assert ex2(10, 10) == 10