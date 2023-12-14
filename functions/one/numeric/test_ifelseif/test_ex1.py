from ..ifelseif.ex1 import ex1

import pytest

def test_ex1_negative():
    assert ex1(-5) == 0

def test_ex1_zero():
    assert ex1(0) == 1

def test_ex1_positive():
    assert ex1(10) == 20

def test_ex1_noninteger():
    assert ex1(1.5) == 3