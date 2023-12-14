from ..ifs.ex3 import ex3

import pytest

def test_ex3_equal_length():
    assert ex3("hello", "world") == "helloworld"

def test_ex3_string1_longer():
    assert ex3("python", "code") == "pythoncode"

def test_ex3_string2_longer():
    assert ex3("code", "python") == "pythoncode"

def test_ex3_empty_string1():
    assert ex3("", "hello") == "hello"

def test_ex3_empty_string2():
    assert ex3("hello", "") == "hello"

def test_ex3_special_characters():
    assert ex3("!", "?") == "!?"

def test_ex3_numbers():
    assert ex3("123", "456") == "123456"

def test_ex3_spaces():
    assert ex3("hello ", "world") == "worldhello "

def test_ex3_empty_strings():
    assert ex3("", "") == ""