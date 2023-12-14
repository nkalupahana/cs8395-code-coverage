from ..none.ex5 import ex5

import pytest

def test_ex5():
  assert ex5("Hello") == "HELLOhello"
  assert ex5("abc") == "ABCabc"
  assert ex5("") == ""