from ..ifs.ex5 import ex5

import pytest
 
def test_ex5_positive():
  assert ex5(5) == 10
  assert ex5(10) == 20
  assert ex5(15) == 30
  
def test_ex5_negative():
  assert ex5(-5) == 10
  assert ex5(-10) == 20
  assert ex5(-15) == 30
  
def test_ex5_zero():
  assert ex5(0) == 0