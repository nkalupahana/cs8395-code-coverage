from ..ifelseif.ex6 import ex6

import pytest

def test_ex6_equal():
  assert ex6(3, 3) == 9

def test_ex6_x_greater():
  assert ex6(5, 3) == 2

def test_ex6_y_greater():
  assert ex6(3, 5) == 2