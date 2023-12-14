from ..ifelseif.ex4 import ex4

import pytest

def test_ex4_empty():
    assert ex4("") is None

def test_ex4_single():
    assert ex4("a") == "A"

def test_ex4_multiple():
    assert ex4("hello") == "Hello"

def test_ex4_numbers():
    assert ex4("123") == "123"

def test_ex4_special_chars():
    assert ex4("!@#$") == "!@#$"

def test_ex4_uppercase():
    assert ex4("HELLO") == "HELLO"

def test_ex4_mixed_case():
    assert ex4("hElLo") == "HElLo"

def test_ex4_whitespace():
    assert ex4(" hello ") == " Hello "