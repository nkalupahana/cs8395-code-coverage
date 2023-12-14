from ..none.ex0 import ex0

import pytest

def test_ex0():
    assert ex0("", "") == ""
    assert ex0("Hello", "World") == "HelloWorld"
    assert ex0("Coding", "is fun") == "Codingis fun"
    assert ex0("I love", "Python") == "I lovePython"
    assert ex0("2", " + 2 = ") == "2 + 2 = "