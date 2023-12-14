from ..ifs.ex8 import ex8

import pytest

def test_ex8():
  assert ex8("hello", "world") == "worldhello"
  assert ex8("python", "pytest") == "pytestpython"
  assert ex8("cat", "dog") == "dogcat"
  assert ex8("123", "456") == "456123"
  assert ex8("", "test") == "test"

def test_ex8_empty():
  assert ex8("", "") == ""

def test_ex8_same_length():
  assert ex8("hello", "there") == "therehello"