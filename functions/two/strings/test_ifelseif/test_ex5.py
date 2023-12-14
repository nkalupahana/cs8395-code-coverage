from ..ifelseif.ex5 import ex5

import pytest

def test_ex5():
    assert ex5("hello", "world") == "helloworld"
    assert ex5("python", "code") == "pythoncode"
    assert ex5("hello", "python") == "pythonhello"
    assert ex5("python", "hello") == "pythonhello"
    assert ex5("hello", "hello") == "ollehhello"