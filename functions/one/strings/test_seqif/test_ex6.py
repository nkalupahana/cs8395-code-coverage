from ..seqif.ex6 import ex6

import pytest

def test_ex6_all_upper():
    assert ex6("HELLO WORLD") == "hello world"

def test_ex6_starts_with_a():
    assert ex6("apple") == "thepple"

def test_ex6_no_changes():
    assert ex6("Hello World") == "Hello World"