from ..nestedif.ex6 import ex6

import pytest

def test_ex6_odd_inputs():
    assert ex6(1, 3) == 2
    assert ex6(5, 1) == 4
    assert ex6(7, 5) == 4
    assert ex6(3, 9) == 6
    assert ex6(11, 15) == 4

def test_ex6_even_inputs():
    assert ex6(2, 4) == 8
    assert ex6(6, 10) == 8
    assert ex6(8, 14) == 12
    assert ex6(12, 18) == 12
    assert ex6(16, 20) == 8

def test_ex6_zero_inputs():
    assert ex6(0, 0) == 0
    assert ex6(0, 10) == 5
    assert ex6(10, 0) == 10
    assert ex6(0, -10) == 5
    assert ex6(-10, 0) == 10

def test_ex6_negative_inputs():
    assert ex6(-5, -10) == 10
    assert ex6(-15, -20) == 8
    assert ex6(-8, -4) == 8
    assert ex6(-12, -6) == 12
    assert ex6(-16, -8) == 8