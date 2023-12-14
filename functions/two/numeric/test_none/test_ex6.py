from ..none.ex6 import ex6

import pytest

def test_ex6():
    assert ex6(1, 2) == 2

def test_ex6_negative():
    assert ex6(-1, -2) == -2

def test_ex6_zero():
    assert ex6(0, 0) == 0