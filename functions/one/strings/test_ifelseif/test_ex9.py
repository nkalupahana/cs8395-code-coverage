from ..ifelseif.ex9 import ex9

import pytest

def test_ex9_long_string():
    assert ex9("This is a long string") == "This i..."

def test_ex9_medium_string():
    assert ex9("Hello") == "Hel..."

def test_ex9_short_string():
    assert ex9("Hi") == ""

def test_ex9_empty_string():
    assert ex9("") == ""