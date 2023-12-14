from ..ifelseif.ex9 import ex9

import pytest

def test_ex9_greater():
    assert ex9(10, 5) == 15

def test_ex9_equal():
    assert ex9(5, 5) == 25

def test_ex9_less():
    assert ex9(5, 10) == -5