from ..nestedif.ex1 import ex1

import pytest

def test_ex1():
  assert ex1("hello", "world") == "worldhello"
  assert ex1("longer", "short") == "shortlonger"
  assert ex1("123", "12") == "12123"
  assert ex1("a", "b") == "ba"
  assert ex1("abcdef", "") == "abcdef"