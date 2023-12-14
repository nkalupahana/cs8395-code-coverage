from ..none.ex4 import ex4

import pytest

def test_ex4():
    assert ex4("hello", "world") == "helloworld"
    assert ex4("abc", "def") == "abcdef"
    assert ex4("123", "456") == "123654"