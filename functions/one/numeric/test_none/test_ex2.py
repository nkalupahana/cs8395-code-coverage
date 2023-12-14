from ..none.ex2 import ex2

import pytest

def test_ex2():
    assert ex2(5) == 6
    assert ex2(10) == 11
    assert ex2(-2) == -1
    assert ex2(0) == 1
    assert ex2(100) == 101