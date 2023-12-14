from ..seqif.ex2 import ex2

import pytest

def test_ex2():
    assert ex2("hello", "lo") == "hel"
    assert ex2("hello", "hello") == ""
    assert ex2("hello", "o") == "hell"
    assert ex2("hello", "world") == "helloworld"