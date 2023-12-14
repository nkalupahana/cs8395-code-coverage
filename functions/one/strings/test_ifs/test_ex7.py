from ..ifs.ex7 import ex7

import pytest

def test_ex7():
    assert ex7("hello") == "hello"
    assert ex7("world") == "WORLD"
    assert ex7("pytest") == "PYTEST"
    assert ex7("code") == "code"
    assert ex7("coverage") == "COVERAGE"

def test_empty_string():
    assert ex7("") == ""

def test_one_letter():
    assert ex7("a") == "a"

def test_five_letters():
    assert ex7("python") == "python"