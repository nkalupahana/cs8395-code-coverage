from ..seqif.ex3 import ex3

import pytest

def test_ex3():
    assert ex3(5, 10) == 10
    assert ex3(10, 5) == 10
    assert ex3(2, 8) == 12
    assert ex3(8, 2) == 12

def test_ex3_small_difference():
    assert ex3(20, 21) == 2
    assert ex3(21, 20) == 2
    assert ex3(3, 4) == 2
    assert ex3(4, 3) == 2

def test_ex3_large_difference():
    assert ex3(50, 10) == 80
    assert ex3(10, 50) == 80
    assert ex3(100, 200) == 200
    assert ex3(200, 100) == 200