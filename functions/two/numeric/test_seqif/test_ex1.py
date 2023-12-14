from ..seqif.ex1 import ex1

import pytest

def test_ex1_greater():
    assert ex1(15, 10) == 15 - 10

def test_ex1_less():
    assert ex1(5, 10) == 10 - 5

def test_ex1_equal():
    assert ex1(10, 10) == 0

def test_ex1_result_greater():
    assert ex1(20, 10) == 20 - 10 + 5

def test_ex1_result_less():
    assert ex1(10, 5) == 5 - 10 + 5