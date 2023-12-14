from ..none.ex4 import ex4

import pytest

def test_ex4():
  assert ex4(0) == 2
  assert ex4(10) == 12
  assert ex4(-5) == -3