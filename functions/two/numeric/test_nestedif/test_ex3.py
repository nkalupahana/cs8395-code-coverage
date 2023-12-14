from ..nestedif.ex3 import ex3

import pytest

def test_ex3():
    assert ex3(5, 3) == 5
    assert ex3(15, 3) == 18
    assert ex3(15, 7) == 22

def test_ex3_if():
    assert ex3(12, 3) == 15
    assert ex3(12, 0) == 12
    assert ex3(15, 4) == 19