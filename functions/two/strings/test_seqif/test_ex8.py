from ..seqif.ex8 import ex8

import pytest

def test_string1_longer():
    assert ex8("hello", "hi") == "hellohi"

def test_string2_longer():
    assert ex8("hi", "hello") == "hihello"

def test_string1_isupper():
    assert ex8("HELLO", "hi") == "hellohi"

def test_string2_isupper():
    assert ex8("hi", "HELLO") == "hihello"

def test_both_strings_are_upper():
    assert ex8("HELLO", "HI") == "hellohi"