from ..ifs.ex4 import ex4

import pytest

def test_ex4_equal():
    assert ex4(5, 5) == 0

def test_ex4_first_greater():
    assert ex4(10, 5) == 5

def test_ex4_second_greater():
    assert ex4(5, 10) == 5