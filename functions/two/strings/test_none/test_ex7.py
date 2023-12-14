from ..none.ex7 import ex7

import pytest

# Test case for empty strings
def test_ex7_empty():
    assert ex7("", "") == ""

# Test case for strings with single character
def test_ex7_single_char():
    assert ex7("a", "b") == "ab"

# Test case for strings with multiple characters
def test_ex7_multi_char():
    assert ex7("hello", "world") == "helloworld"

# Test case for strings with special characters
def test_ex7_special_chars():
    assert ex7("!@#", "$%^") == "!@#$%^"

# Test case for strings with numerical characters
def test_ex7_numeric_chars():
    assert ex7("123", "456") == "123456"

# Test case for strings with spaces
def test_ex7_spaces():
    assert ex7("Hello ", "World") == "Hello World"