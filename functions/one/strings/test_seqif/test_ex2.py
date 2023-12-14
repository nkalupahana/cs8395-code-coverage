from ..seqif.ex2 import ex2

import pytest

def test_ex2_upper():
    assert ex2("HELLO") == "HELLO"

def test_ex2_lower():
    assert ex2("hi") == "hi"

def test_ex2_mixed_case():
    assert ex2("PyTHon") == "PYTHON"

def test_ex2_empty_string():
    assert ex2("") == ""

def test_ex2_single_character():
    assert ex2("a") == "a"

def test_ex2_long_string():
    assert ex2("this is a very long string") == "THIS IS A VERY LONG STRING"