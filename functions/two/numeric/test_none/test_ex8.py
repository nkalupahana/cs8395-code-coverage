from ..none.ex8 import ex8

import pytest

def test_ex8():
    assert ex8(5, 10) == 0
    assert ex8(10, 5) == 0
    assert ex8(5, 5) == 0