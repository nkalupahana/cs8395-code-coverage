from ..nestedif.ex9 import ex9

import pytest

def test_num_greater():
    assert ex9(5, 3) == 2

def test_num_less():
    assert ex9(2, 5) == 3

def test_same_num():
    assert ex9(5, 5) == 0

def test_floats():
    assert ex9(5.5, 3.8) == 1.7

def test_negative_nums():
    assert ex9(-5, -3) == 2

def test_mixed_nums():
    assert ex9(-5, 3) == 8