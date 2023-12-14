from ..seqif.ex9 import ex9

import pytest

def test_ex9():
  assert ex9("1234567890") == "1234567890"
  assert ex9("1234567890123456") == "5678901234"
  assert ex9("abc") == "ABC"
  assert ex9("") == ""