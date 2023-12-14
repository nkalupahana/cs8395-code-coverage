from ..nestedif.ex7 import ex7

import pytest

def test_longer_string():
    string1 = "Hello"
    string2 = "World"
    assert ex7(string1, string2) == "HelloWorld"

def test_shorter_string():
    string1 = "Hi"
    string2 = "Hey"
    assert ex7(string1, string2) == "HeyHi"

def test_short_string():
    string1 = "Hello"
    string2 = "Hi"
    assert ex7(string1, string2) == "HelloHello"

def test_empty_string():
    string1 = ""
    string2 = "World"
    assert ex7(string1, string2) == "World"

def test_equal_length_strings():
    string1 = "Hello"
    string2 = "Hey"
    assert ex7(string1, string2) == "HelloHey"