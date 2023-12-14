from ..seqif.ex0 import ex0

import pytest

def test_ex0():
    assert ex0("hello") == "hello"

def test_ex0_upper():
    assert ex0("hello world") == "HELLO WORLD"

def test_ex0_lower():
    assert ex0("hi") == "hi"