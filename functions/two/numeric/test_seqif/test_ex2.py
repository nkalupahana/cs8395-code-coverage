from ..seqif.ex2 import ex2

import pytest

def test_ex2_greater():
    result = ex2(10, 5)
    assert result == 10

def test_ex2_less():
    result = ex2(5, 10)
    assert result == 10

def test_ex2_equal():
    result = ex2(5, 5)
    assert result == 0

def test_ex2_greater_than_5():
    result = ex2(10, 5)
    assert result > 5

def test_ex2_less_than_5():
    result = ex2(5, 10)
    assert result < 5

def test_ex2_equal_to_5():
    result = ex2(5, 5)
    assert result == 0

def test_ex2_result_doubled():
    result = ex2(10, 5)
    assert result == 20

def test_ex2_result_halved():
    result = ex2(5, 10)
    assert result == 5

def test_ex2_result_not_doubled():
    result = ex2(4, 2)
    assert result == 2

def test_ex2_result_not_halved():
    result = ex2(2, 4)
    assert result == 1

def test_ex2_result_not_greater_than_5():
    result = ex2(4, 2)
    assert result < 5

def test_ex2_result_not_less_than_5():
    result = ex2(2, 4)
    assert result > 5