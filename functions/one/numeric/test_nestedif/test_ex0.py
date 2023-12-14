from ..nestedif.ex0 import ex0

import pytest

def test_ex0():
  assert ex0(0) == 0
  assert ex0(1) == 2
  assert ex0(2) == 6
  assert ex0(3) == 4
  assert ex0(4) == 8
  assert ex0(-1) == -1