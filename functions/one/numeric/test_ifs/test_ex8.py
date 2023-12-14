from ..ifs.ex8 import ex8

import pytest

def test_ex8():
    assert ex8(0) == -1
    assert ex8(-5) == -6
    assert ex8(10) == 11
    assert ex8(100) == 101