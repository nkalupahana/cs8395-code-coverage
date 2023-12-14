from ..none.ex3 import ex3

import pytest

def test_ex3():
    assert ex3(5, 2) == 3
    assert ex3(10, 5) == 5
    assert ex3(0, 0) == 0
    assert ex3(-5, -10) == 5
    assert ex3(2.5, 1.5) == 1

def test_ex3_negative():
    assert ex3(-5, 2) == -7
    assert ex3(10, -5) == 15
    assert ex3(-2.5, -1.5) == -1

def test_ex3_zero():
    assert ex3(0, 5) == -5
    assert ex3(5, 0) == 5
    assert ex3(0, -10) == 10

def test_ex3_decimals():
    assert ex3(2.5, 1.2) == 1.3
    assert ex3(5.5, 2.5) == 3

def test_ex3_large_numbers():
    assert ex3(1000000, 500000) == 500000
    assert ex3(1000000000, 999999999) == 1

def test_ex3_mixed():
    assert ex3(-5, 2.5) == -7.5
    assert ex3(10.5, -5) == 15.5
    assert ex3(0, -1.5) == 1.5