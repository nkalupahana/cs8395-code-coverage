from ..seqif.ex4 import ex4

import pytest

def test_ex4_positive():
  assert ex4(5) == 2
  
def test_ex4_negative():
  assert ex4(-2) == 1
  
def test_ex4_zero():
  assert ex4(0) == 2