from ..ifs.ex1 import ex1

import pytest

def test_ex1():
    assert ex1("hello", "world") == "worldhello"

def test_ex1_same_length():
    assert ex1("hello", "goodbye") == "hellogoodbye"

def test_ex1_empty_string():
    assert ex1("", "hello") == "hello"

def test_ex1_same_string():
    assert ex1("hello", "hello") == "hellohello"

def test_ex1_empty_strings():
    assert ex1("", "") == ""