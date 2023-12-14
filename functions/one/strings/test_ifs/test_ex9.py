from ..ifs.ex9 import ex9

import pytest

def test_ex9_upper():
    assert ex9("hello world") == "HELLO WORLD"

def test_ex9_lower():
    assert ex9("hello") == "hello"

def test_ex9_empty():
    assert ex9("") == ""