from ..nestedif.ex2 import ex2

# Sample pytest code
import pytest

# Test case 1: String length greater than 10 and starts with "A"
def test_ex2_long_start_with_A():
  string = "apple pie is delicious"
  expected_result = "ZPPLE PIE IS DELICIOUS"
  assert ex2(string) == expected_result

# Test case 2: String length greater than 10 and does not start with "A"
def test_ex2_long_not_start_with_A():
  string = "python is awesome"
  expected_result = "PYTHON IS AWESOME"
  assert ex2(string) == expected_result

# Test case 3: String length less than 10
def test_ex2_short():
  string = "hello"
  expected_result = "hello"
  assert ex2(string) == expected_result