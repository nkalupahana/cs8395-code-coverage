from ..none.ex9 import ex9

import pytest

def test_ex9_empty_string():
    assert ex9("") == ""

def test_ex9_single_char():
    assert ex9("a") == "a"

def test_ex9_long_string():
    assert ex9("abcdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedcba"

def test_ex9_numbers():
    assert ex9("1234567890") == "0987654321"

def test_ex9_special_chars():
    assert ex9("!@#$%^&*()_+{}:\"<>?,./;'[]\\|-=") == "-=|\\][]';/.>,<\":}{+_)(*&^%$#@!"