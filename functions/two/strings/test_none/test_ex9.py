from ..none.ex9 import ex9

import pytest

@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ("hello", "world", "held"),
        ("goodbye", "python", "goyt"),
        ("", "test", "es"),
        ("12345", "abcde", "12de"),
        ("apple", "banana", "apna"),
    ]
)
def test_ex9(str1, str2, expected):
    assert ex9(str1, str2) == expected