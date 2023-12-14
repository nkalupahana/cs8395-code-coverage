from ..ifelseif.ex4 import ex4

# Generated Tests


import pytest

def test_ex4():
    assert ex4("abc", "def") == "abcdef"
    assert ex4("abc", "") == "abc"
    assert ex4("", "def") == "def"
    assert ex4("", "") == " "
    assert ex4("longString", "short") == "longStringshort"
    assert ex4("short", "longString") == "longStringshort"
