from ..none.ex8 import ex8

import pytest

def test_ex8():
    # Test case 1
    assert ex8("Hello ", "World") == "Hello World"

    # Test case 2
    assert ex8("1", "2") == "12"

    # Test case 3
    assert ex8("", "") == ""

    # Test case 4
    assert ex8("Python", " is awesome") == "Python is awesome"

    # Test case 5
    assert ex8("The answer is ", "42") == "The answer is 42"