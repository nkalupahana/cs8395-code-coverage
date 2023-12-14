from ..nestedif.ex8 import ex8

import pytest

def test_ex8_longer_string():
    assert ex8("hello", "world") == "helloworld"

def test_ex8_equal_length():
    assert ex8("hello", "goodbye") == "hellogoodbye!"

def test_ex8_shorter_string():
    assert ex8("cat", "dog") == "dogcat"

def test_ex8_empty_string():
    assert ex8("", "hello") == "hello"

def test_ex8_longer_string_reversed():
    assert ex8("world", "hello") == "worldhello"

def test_ex8_equal_length_reversed():
    assert ex8("goodbye", "hello") == "goodbyehello!"

def test_ex8_shorter_string_reversed():
    assert ex8("dog", "cat") == "catdog"