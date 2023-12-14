from ..ifs.ex4 import ex4

import pytest

def test_ex4():
    # Test string with spaces
    assert ex4("Hello World") == "Hello-World"
    # Test string with no spaces
    assert ex4("Hello") == "Hello"
    # Test empty string
    assert ex4("") == ""
    # Test string with special characters
    assert ex4("Hello!@#$%") == "Hello!@#$%"