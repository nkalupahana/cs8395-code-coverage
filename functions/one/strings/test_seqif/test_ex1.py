from ..seqif.ex1 import ex1

import pytest

def test_even_string():
    string = "TEST"
    assert ex1(string) == "TEST"

def test_odd_string():
    string = "test"
    assert ex1(string) == "test"

def test_empty_string():
    string = ""
    assert ex1(string) == ""

def test_numbers_string():
    string = "12345"
    assert ex1(string) == "12345"