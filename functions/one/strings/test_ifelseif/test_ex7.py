from ..ifelseif.ex7 import ex7

import pytest

def test_ex7_long_string():
  assert ex7("hello world") == "HELLO WORLD"

def test_ex7_short_string():
  assert ex7("hi") == "hi"

def test_ex7_reverse_string():
  assert ex7("python") == "nohtyp"

def test_ex7_empty_string():
  assert ex7("") == ""

def test_ex7_numbers_only():
  assert ex7("12345") == "12345"

def test_ex7_special_characters():
  assert ex7("!@#$%") == "!@#$%"

def test_ex7_mixed_case():
  assert ex7("HeLlO") == "HELLO"