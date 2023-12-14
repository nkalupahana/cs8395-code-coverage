from ..nestedif.ex9 import ex9

import pytest

def test_ex9():
  assert ex9("hello world") == "HELLO WORLD"
  assert ex9("hello") == "hello"
  assert ex9("apple") == "APPLE!"