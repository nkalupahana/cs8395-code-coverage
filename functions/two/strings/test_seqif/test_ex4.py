from ..seqif.ex4 import ex4

import pytest

def test_ex4_longer_first():
    assert ex4("hello", "hi") == "hellohi"

def test_ex4_longer_second():
    assert ex4("hi", "hello") == "hihello"

def test_ex4_equal_length():
    assert ex4("hello", "world") == "helloworld"

def test_ex4_empty_str():
    assert ex4("", "hello") == "hello"

def test_ex4_same_str():
    assert ex4("hello", "hello") == "hellohello"