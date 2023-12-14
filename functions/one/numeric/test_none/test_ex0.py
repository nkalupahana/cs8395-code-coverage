from ..none.ex0 import ex0

import pytest

def test_ex0():
  assert ex0(10) == 40
  assert ex0(0) == 30
  assert ex0(-10) == 20