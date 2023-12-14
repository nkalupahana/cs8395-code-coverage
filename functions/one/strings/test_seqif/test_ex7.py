from ..seqif.ex7 import ex7

import pytest

def test_ex7():
    # Test string with length > 5
    assert ex7("hello") == "HELLO"
    assert ex7("goodbye") == "GOODBYE"

    # Test string starting with "A"
    assert ex7("apple") == "Apple"
    assert ex7("awesome") == "Awesome"

    # Test string with length <= 5 and not starting with "A"
    assert ex7("hi") == "hi"
    assert ex7("python") == "python"

    # Test empty string
    assert ex7("") == ""

    # Test string with only one character
    assert ex7("a") == "a"
    assert ex7("A") == "A"