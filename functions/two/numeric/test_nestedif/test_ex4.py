from ..nestedif.ex4 import ex4

import pytest

def test_ex4_positive_numbers():
    assert ex4(2, 3) == 13
    assert ex4(5, 7) == 74

def test_ex4_negative_numbers():
    assert ex4(-2, -3) == -35
    assert ex4(-5, -7) == -172

def test_ex4_mixed_numbers():
    assert ex4(2, -3) == -1
    assert ex4(-5, 7) == 28