from ..ifelseif.ex0 import ex0

import pytest

# Test that the function returns the correct output for strings of equal length
def test_ex0_equal():
    assert ex0("hello", "world") == "helloworld"

# Test that the function returns the correct output when the first string is longer than the second
def test_ex0_first_longer():
    assert ex0("hello", "hi") == "hihello"

# Test that the function returns the correct output when the second string is longer than the first
def test_ex0_second_longer():
    assert ex0("hi", "hello") == "hihello"