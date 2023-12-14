from ..seqif.ex5 import ex5

import pytest

def test_ex5_positive():
  assert ex5(5) == 50

def test_ex5_zero():
  assert ex5(0) == 0