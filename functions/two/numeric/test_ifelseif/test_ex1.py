from ..ifelseif.ex1 import ex1

import pytest

def test_ex1():
  assert ex1(3, 5) == 8
  assert ex1(5, 3) == 2
  assert ex1(3, 3) == 9