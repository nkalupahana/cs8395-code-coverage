from ..ifs.ex5 import ex5

import pytest

def test_ex5_upper():
    assert ex5("HELLO WORLD") == "HELLO WORLD"

def test_ex5_lower():
    assert ex5("hello") == "hello"