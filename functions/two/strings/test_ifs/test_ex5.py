from ..ifs.ex5 import ex5

import pytest

@pytest.mark.parametrize("string1, string2, expected", [
    ("hello", "world", "hello world"),
    ("hello", "python", "hello python"),
    ("python", "is", "python is"),
    ("python", "awesome", "python awesome"),
])
def test_ex5(string1, string2, expected):
    assert ex5(string1, string2) == expected

@pytest.mark.parametrize("string1, string2, expected", [
    ("hello", "world", "HELLO WORLD"),
    ("hello", "python", "HELLO PYTHON"),
    ("python", "is", "PYTHON IS"),
    ("python", "awesome", "PYTHON AWESOME"),
])
def test_ex5_upper(string1, string2, expected):
    assert ex5(string1, string2).upper() == expected