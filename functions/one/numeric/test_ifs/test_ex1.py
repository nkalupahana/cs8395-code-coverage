from ..ifs.ex1 import ex1

import pytest

def test_ex1_positive():
  assert ex1(5) == 10

def test_ex1_negative():
  assert ex1(-5) == -7

def test_ex1_zero():
  assert ex1(0) == -2