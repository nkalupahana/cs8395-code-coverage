from ..ifelseif.ex7 import ex7

import pytest

def test_ex7_equal_length():
    assert ex7("hello", "world") == "helloworld"

def test_ex7_string1_longer():
    assert ex7("testing", "python") == "testingpython"

def test_ex7_string2_longer():
    assert ex7("python", "testing") == "pythontesting"

def test_ex7_empty_strings():
    assert ex7("", "") == ""

def test_ex7_one_empty_string():
    assert ex7("hello", "") == "hello"

def test_ex7_one_empty_string():
    assert ex7("", "world") == "world"