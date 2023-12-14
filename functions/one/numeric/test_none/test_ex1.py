from ..none.ex1 import ex1

import pytest

def test_ex1():
  assert ex1(5) == 7
  assert ex1(-5) == -3
  assert ex1(0) == 2
  assert ex1(10) == 12