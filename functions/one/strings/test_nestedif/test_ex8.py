from ..nestedif.ex8 import ex8

import pytest

def test_ex8_upper():
  assert ex8("hello") == "HELLO"
  
def test_ex8_lower():
  assert ex8("hello world") == "HELLO WORLD"
  
def test_ex8_first_a():
  assert ex8("apple") == "PPLE"
  
def test_ex8_no_changes():
  assert ex8("python") == "python"