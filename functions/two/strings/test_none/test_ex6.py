from ..none.ex6 import ex6

import pytest

def test_ex6():
    assert ex6("Hello", "World") == "HelloWorld"
    assert ex6("abc", "123") == "abc123"
    assert ex6("", "") == ""