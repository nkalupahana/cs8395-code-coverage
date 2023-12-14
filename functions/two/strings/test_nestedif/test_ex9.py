from ..nestedif.ex9 import ex9

import pytest

def test_ex9_equal_strings():
    assert ex9("hello", "hello") == "hellohello"

def test_ex9_longer_string1():
    assert ex9("python", "code") == "codepython"

def test_ex9_longer_string2():
    assert ex9("pytest", "tests") == "testspytest"

def test_ex9_longer_string1_over_5():
    assert ex9("testing", "py") == "gnitsetpy"