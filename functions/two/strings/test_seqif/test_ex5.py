from ..seqif.ex5 import ex5

import pytest

def test_ex5():
    assert ex5("hello", "world") == "WORLDhello"
    assert ex5("hello", "hi") == "helloHI"
    assert ex5("python", "programming") == "programmingPYTHON"
    assert ex5("abc", "def") == "abcDEF"
    assert ex5("a", "b") == "AB"