from ..none.ex6 import ex6

import pytest

def test_ex6():
    assert ex6(0) == -2
    assert ex6(5) == 3
    assert ex6(10) == 8
    assert ex6(-5) == -7
    assert ex6(3.14) == 1.14