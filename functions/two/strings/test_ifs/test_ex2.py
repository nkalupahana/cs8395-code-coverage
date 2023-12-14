from ..ifs.ex2 import ex2

import pytest

def test_ex2():
    assert ex2("abc", "def") == "abcdef"
    assert ex2("longstring", "short") == "shortlongstring"
    assert ex2("equal", "length") == "equallength"
    assert ex2("", "empty") == "empty"
    assert ex2(" ", "space") == " space"