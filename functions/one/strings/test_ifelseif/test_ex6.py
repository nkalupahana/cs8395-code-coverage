from ..ifelseif.ex6 import ex6

import pytest

def test_ex6():
  # Test lowercase string
  result = ex6("hello")
  assert result == "hello"
  
  # Test string with 'a' in it
  result = ex6("apple")
  assert result == "APPLE"
  
  # Test string with 'e' in it
  result = ex6("elephant")
  assert result == "Elephant"
  
  # Test string with both 'a' and 'e' in it
  result = ex6("banana")
  assert result == "BANANA"
  
  # Test empty string
  result = ex6("")
  assert result == ""