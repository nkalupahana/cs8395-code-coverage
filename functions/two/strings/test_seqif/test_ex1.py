from ..seqif.ex1 import ex1

import pytest

def test_len_string_greater():
    assert ex1("hello", "world") == "helloworld"

def test_len_string_less():
    assert ex1("helloworld", "hello") == "helloworld"