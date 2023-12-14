from ..ifs.ex0 import ex0

import pytest

def test_ex0_empty_string():
  assert ex0("") == ""

def test_ex0_lowercase_string():
  assert ex0("hello") == "HELLO"

def test_ex0_uppercase_string():
  assert ex0("WORLD") == "WORLD"

def test_ex0_mixed_case_string():
  assert ex0("hElLo") == "HELLO"