from ..ifelseif.ex0 import ex0

import pytest

def test_ex0_equal():
    assert ex0(5, 5) == 0

def test_ex0_greater():
    assert ex0(10, 5) == 5

def test_ex0_less():
    assert ex0(5, 10) == 5