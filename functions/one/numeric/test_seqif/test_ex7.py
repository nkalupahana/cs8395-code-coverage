from ..seqif.ex7 import ex7

import pytest

def test_ex7():
  assert ex7(5) == 10
  assert ex7(10) == 5
  assert ex7(-5) == -5