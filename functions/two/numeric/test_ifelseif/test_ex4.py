from ..ifelseif.ex4 import ex4

import pytest

def ex4(x, y):
  if x > y:
    result = x + y
  elif x == y:
    result = x * y
  else:
    result = x - y

  return result

def test_ex4_greater():
  assert ex4(5, 3) == 8

def test_ex4_equal():
  assert ex4(3, 3) == 9

def test_ex4_less():
  assert ex4(3, 5) == -2

def test_ex4_invalid():
  with pytest.raises(TypeError):
    ex4("a", 2)