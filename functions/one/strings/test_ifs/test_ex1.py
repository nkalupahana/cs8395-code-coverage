from ..ifs.ex1 import ex1

import pytest

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hello", "hello"),
        ("Python", "PYTHON"),
        ("", ""),
        ("12345", "12345"),
        ("This is a long string", "THIS IS A LONG STRING"),
    ],
)
def test_ex1(input_string, expected_output):
    assert ex1(input_string) == expected_output