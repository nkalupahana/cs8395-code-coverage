from ..none.ex3 import ex3

import pytest

def test_ex3_upper():
    assert ex3("hello") == "HELLOhello"

def test_ex3_lower():
    assert ex3("WORLD") == "WORLDworld"

def test_ex3_mixed():
    assert ex3("PyThOn") == "PYTHONpython"