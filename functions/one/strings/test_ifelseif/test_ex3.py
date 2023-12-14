from ..ifelseif.ex3 import ex3

import pytest

def test_ex3_upper():
    assert ex3("hello world") == "HELLO WORLD"

def test_ex3_lower():
    assert ex3("hi") == "hi"

def test_ex3_title():
    assert ex3("goodbye") == "Goodbye"

def test_ex3_empty():
    assert ex3("") == ""