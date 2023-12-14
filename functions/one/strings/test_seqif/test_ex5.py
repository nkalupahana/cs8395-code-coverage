from ..seqif.ex5 import ex5

import pytest

# Test if string length is less than or equal to 6
def test_string_length_less_than_or_equal_to_6():
    string = "HELLO"
    assert ex5(string) == "HELLO"

# Test if string length is greater than 6
def test_string_length_greater_than_6():
    string = "hello world"
    assert ex5(string) == "hello world"