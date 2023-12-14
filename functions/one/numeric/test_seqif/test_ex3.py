from ..seqif.ex3 import ex3

import pytest

def test_ex3_positive():
  assert ex3(10) == 5
  
def test_ex3_negative():
  assert ex3(-10) == -7
  
def test_ex3_zero():
  assert ex3(0) == 3