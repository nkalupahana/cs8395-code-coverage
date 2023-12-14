from ..nestedif.ex6 import ex6

import pytest

def test_ex6_long_string():
    assert ex6("abcdef") == "fedcbas"

def test_ex6_short_string():
    assert ex6("abc") == "abcs"

def test_ex6_empty_string():
    assert ex6("") == "s"

def test_ex6_string_with_s():
    assert ex6("hello") == "hello"