from ..nestedif.ex4 import ex4

import pytest 

def test_ex4_even_divisible_by_4():
  num = 8
  assert ex4(num) == 2

def test_ex4_even_not_divisible_by_4():
  num = 6
  assert ex4(num) == 3