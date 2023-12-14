from ..seqif.ex0 import ex0

import pytest

def test_ex0():
  assert ex0(10, 5) == 10
  assert ex0(5, 10) == 10
  assert ex0(8, 6) == 4
  assert ex0(6, 8) == 4
  assert ex0(2, 7) == 10
  assert ex0(7, 2) == 10
  assert ex0(1, 10) == 18
  assert ex0(10, 1) == 18
  assert ex0(3, 8) == 10
  assert ex0(8, 3) == 10
  assert ex0(6, 4) == 4
  assert ex0(4, 6) == 4
  assert ex0(5, 5) == 10