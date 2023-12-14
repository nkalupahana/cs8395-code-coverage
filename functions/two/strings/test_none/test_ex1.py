from ..none.ex1 import ex1

import pytest

def test_ex1():
    assert ex1("hello", "world") == "helloworld"