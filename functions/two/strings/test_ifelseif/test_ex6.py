from ..ifelseif.ex6 import ex6

import pytest

# Test case for equal length strings
def test_equal_length_strings():
    string1 = "abc"
    string2 = "def"
    assert ex6(string1, string2) == "abcdef"

# Test case for string1 longer than string2
def test_string1_longer():
    string1 = "abcd"
    string2 = "ef"
    assert ex6(string1, string2) == "abce"

# Test case for string2 longer than string1
def test_string2_longer():
    string1 = "ab"
    string2 = "cdef"
    assert ex6(string1, string2) == "abc" 

# Test case for empty strings
def test_empty_strings():
    string1 = ""
    string2 = ""
    assert ex6(string1, string2) == ""

# Test case for strings with spaces
def test_strings_with_spaces():
    string1 = "abc "
    string2 = "defg"
    assert ex6(string1, string2) == "abc def"

# Test case for strings with special characters
def test_strings_with_special_characters():
    string1 = "abc$"
    string2 = "defg@"
    assert ex6(string1, string2) == "abc$defg@"