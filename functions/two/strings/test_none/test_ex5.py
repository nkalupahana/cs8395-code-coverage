from ..none.ex5 import ex5

import pytest

def test_ex5():
    string1 = "Hello "
    string2 = "World"
    assert ex5(string1, string2) == "Hello World"