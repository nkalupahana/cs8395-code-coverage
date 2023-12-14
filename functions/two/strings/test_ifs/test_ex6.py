from ..ifs.ex6 import ex6

import pytest

def test_len_not_equal():
    assert ex6("hello", "world") == "helloworld"

def test_len_equal():
    assert ex6("python", "code") == "codepython"