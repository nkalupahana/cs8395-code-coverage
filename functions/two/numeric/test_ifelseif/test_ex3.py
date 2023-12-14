from ..ifelseif.ex3 import ex3

import pytest

def test_ex3_equal():
    assert ex3(5, 5) == 0

def test_ex3_greater():
    assert ex3(10, 5) == 5

def test_ex3_less():
    assert ex3(5, 10) == 5