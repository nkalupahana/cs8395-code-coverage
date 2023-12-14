from ..none.ex5 import ex5

import pytest

def test_ex5():
  assert ex5(5, 3) == 2
  assert ex5(10, 5) == 5
  assert ex5(0, 0) == 0
  assert ex5(-5, 2) == -7