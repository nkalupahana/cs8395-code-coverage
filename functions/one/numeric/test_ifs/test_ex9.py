from ..ifs.ex9 import ex9

import pytest

def test_ex9_greater_than_10():
  assert ex9(11) == 16

def test_ex9_equal_to_10():
  assert ex9(10) == 10

def test_ex9_less_than_10():
  assert ex9(9) == 9