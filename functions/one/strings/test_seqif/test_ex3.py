from ..seqif.ex3 import ex3

import pytest

def test_string_length_greater_than_5():
    assert ex3("hello world") == "hello world"

def test_string_length_less_than_or_equal_to_5():
    assert ex3("hi") == "HI"

def test_string_length_equal_to_5():
    assert ex3("12345") == "12345"

def test_empty_string():
    assert ex3("") == ""