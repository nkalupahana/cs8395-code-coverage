from ..ifs.ex4 import ex4

import pytest

def test_ex4_long_first():
  string1 = "hello"
  string2 = "world"
  assert ex4(string1, string2) == "helloworld"

def test_ex4_long_second():
  string1 = "world"
  string2 = "hello"
  assert ex4(string1, string2) == "helloworld"

def test_ex4_equal_length():
  string1 = "hello"
  string2 = "bye"
  assert ex4(string1, string2) == "hellobye"

def test_ex4_empty_string():
  string1 = ""
  string2 = "hello"
  assert ex4(string1, string2) == "hello"

def test_ex4_empty_strings():
  string1 = ""
  string2 = ""
  assert ex4(string1, string2) == ""