from ..ifs.ex2 import ex2

import pytest

def test_ex2():
  assert ex2(1, 2) == 3
  assert ex2(5, 3) == 8
  assert ex2(10, 10) == 20
  assert ex2(-5, 10) == 10
  assert ex2(0, 0) == 0
  assert ex2(100, 50) == 150
  assert ex2(-10, -20) == -30
  assert ex2(2, -4) == -2