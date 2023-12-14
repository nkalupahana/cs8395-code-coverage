from ..none.ex3 import ex3

import pytest

def test_ex3():
  # Test case 1
  assert ex3(5) == 6

  # Test case 2
  assert ex3(-2) == -1

  # Test case 3
  assert ex3(0) == 1