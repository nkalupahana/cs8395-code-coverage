from ..nestedif.ex4 import ex4

import pytest

def test_ex4_long_string():
    assert ex4("Hello World") == "dlroW+olleH"

def test_ex4_short_string():
    assert ex4("Hi") == "Hi"