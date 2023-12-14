from ..ifelseif.ex2 import ex2

import pytest

def test_ex2_upper():
    assert ex2("hello world") == "HELLO WORLD"

def test_ex2_lower():
    assert ex2("hello") == "hello"

def test_ex2_addition():
    assert ex2("hi") == "hi!"