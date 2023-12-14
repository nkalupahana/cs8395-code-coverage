from ..ifelseif.ex8 import ex8

import pytest

@pytest.mark.parametrize("string1, string2, expected", [
    ("hello", "world", "worldhello"),
    ("cat", "dog", "dogcat"),
    ("python", "code", "python code"),
    ("", "", " "),
    ("hi", "", "hi"),
    ("", "test", "test")
])
def test_ex8(string1, string2, expected):
    assert ex8(string1, string2) == expected
    
def test_ex8_empty_strings():
    assert ex8("", "") == " "
    
def test_ex8_long_strings():
    assert ex8("supercalifragilisticexpialidocious", "antidisestablishmentarianism") == "antidisestablishmentarianismsupercalifragilisticexpialidocious"