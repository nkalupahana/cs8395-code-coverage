from ..nestedif.ex3 import ex3

import pytest

def test_ex3_same_length():
    assert ex3("abc", "def") == "abcdef"

def test_ex3_longer_string1():
    assert ex3("abc", "d") == "abcd"

def test_ex3_longer_string2():
    assert ex3("a", "bcde") == "abcde"

def test_ex3_equal_strings():
    assert ex3("abc", "abc") == "abcabc"