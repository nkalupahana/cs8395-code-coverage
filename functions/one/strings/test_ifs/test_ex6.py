from ..ifs.ex6 import ex6

import pytest

# Test that the function returns the string in uppercase if the length is greater than 5
def test_uppercase():
    assert ex6("hello") == "HELLO"
    assert ex6("python") == "PYTHON"

# Test that the function returns the original string if the length is less than or equal to 5
def test_original_string():
    assert ex6("hi") == "hi"
    assert ex6("code") == "code"

# Test that the function returns the original string if the input is an empty string
def test_empty_string():
    assert ex6("") == ""

# Test that the function can handle special characters
def test_special_characters():
    assert ex6("@#$%") == "@#$%"

# Test that the function can handle strings with spaces
def test_string_with_spaces():
    assert ex6("hello world") == "HELLO WORLD"