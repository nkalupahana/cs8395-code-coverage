from ..none.ex7 import ex7

import pytest

def test_ex7():
    assert ex7(0) == 5
    assert ex7(10) == 15
    assert ex7(-5) == 0
    assert ex7(100) == 105

def test_ex7_edge_cases():
    assert ex7(5) == 10
    assert ex7(-10) == -5
    assert ex7(0.5) == 5.5
    assert ex7(-0.5) == 4.5
    assert ex7(2.5) == 7.5
    assert ex7(-2.5) == 2.5
    assert ex7(100.5) == 105.5
    assert ex7(-100.5) == -95.5