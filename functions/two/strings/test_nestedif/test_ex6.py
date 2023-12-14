from ..nestedif.ex6 import ex6

import pytest

@pytest.mark.parametrize("string1, string2, expected", [
    ("hello", "world", "hellohello"),
    ("goodbye", "friend", "goodbyefriend"),
    ("python", "code", "pythoncode"),
    ("", "", ""),
    ("thisisalongstring", "short", "thisishort")
])

def test_ex6(string1, string2, expected):
    assert ex6(string1, string2) == expected

def test_ex6_equal_length():
    assert ex6("same", "length") == "samelength"

def test_ex6_string1_longer():
    assert ex6("longerstring", "short") == "longershort"

def test_ex6_string2_longer():
    assert ex6("short", "longerstring") == "shortlongerstring"

def test_ex6_empty_string1():
    assert ex6("", "world") == "world"

def test_ex6_empty_string2():
    assert ex6("hello", "") == "hello"