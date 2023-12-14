from ..seqif.ex4 import ex4

import pytest

def test_ex4_upper():
    assert ex4("Hello World") == "HELLO WORLD"

def test_ex4_lower():
    assert ex4("Hello") == "hello"

def test_ex4_empty():
    assert ex4("") == ""