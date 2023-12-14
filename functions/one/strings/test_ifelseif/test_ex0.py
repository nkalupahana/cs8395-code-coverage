from ..ifelseif.ex0 import ex0

import pytest

def test_ex0():
    assert ex0("") == "Empty string"
    assert ex0("abc") == "cba"
    assert ex0("a") == "A"
    assert ex0("abcd") == "dcba"