from ..ifs.ex3 import ex3

import pytest

def test_ex3():
  # Arrange
  string = "hello"
  
  # Act
  result = ex3(string)
  
  # Assert
  assert result == "hello5"
  
def test_ex3_empty_string():
  # Arrange
  string = ""
  
  # Act
  result = ex3(string)
  
  # Assert
  assert result == "0"