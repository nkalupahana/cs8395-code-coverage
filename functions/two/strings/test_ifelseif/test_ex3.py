from ..ifelseif.ex3 import ex3

import pytest

def test_ex3_equal_length():
    assert ex3("hello", "world") == "helloworld"

def test_ex3_string1_longer():
    assert ex3("python", "code") == "PYTHONcode"

def test_ex3_string2_longer():
    assert ex3("hello", "there") == "helloTHERE"

def test_ex3_empty_string():
    assert ex3("", "") == ""

def test_ex3_single_letter():
    assert ex3("a", "b") == "ab"

def test_ex3_numbers():
    assert ex3("123", "456") == "123456"

def test_ex3_symbols():
    assert ex3("!@#", "$%^") == "!@#$%^"