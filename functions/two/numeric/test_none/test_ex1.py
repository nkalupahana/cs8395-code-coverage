from ..none.ex1 import ex1

import pytest

def test_ex1():
    assert ex1(3, 4) == 2
    assert ex1(10, -2) == 13
    assert ex1(0, 0) == -5
    assert ex1(-10, -20) == 5