from ..seqif.ex0 import ex0

import pytest

def test_ex0_upper():
    assert ex0("hello", "world") == "HELLOWORLD"

def test_ex0_lower():
    assert ex0("abc", "defg") == "DEFGABC"

def test_ex0_equal():
    assert ex0("python", "pytest") == "PYTESTPYTHON"

def test_ex0_invalid_input():
    assert ex0("123", "456") == "Error"

def test_ex0_empty_strings():
    assert ex0("", "") == "Error"