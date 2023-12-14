from ..ifelseif.ex9 import ex9

import pytest

def test_ex9_equal_strings():
    string1 = "hello"
    string2 = "world"
    assert ex9(string1, string2) == "helloworld"

def test_ex9_string1_longer():
    string1 = "python"
    string2 = "code"
    assert ex9(string1, string2) == "pythoncode"

def test_ex9_string2_longer():
    string1 = "apple"
    string2 = "banana"
    assert ex9(string1, string2) == "applebanana"

def test_ex9_empty_string():
    string1 = ""
    string2 = "pytest"
    assert ex9(string1, string2) == "pytest"