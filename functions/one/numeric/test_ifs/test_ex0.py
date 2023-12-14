from ..ifs.ex0 import ex0

import pytest

def test_ex0():
  x = 5
  assert ex0(x) == 5
  x = 10
  assert ex0(x) == 20
  x = 15
  assert ex0(x) == 30