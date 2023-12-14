from ..none.ex8 import ex8

import pytest

def test_ex8():
    assert ex8("Hello World") == "dlroW olleH"
    assert ex8("12345") == "54321"
    assert ex8("abcde") == "edcba"
    assert ex8("") == ""
    assert ex8("a") == "a"