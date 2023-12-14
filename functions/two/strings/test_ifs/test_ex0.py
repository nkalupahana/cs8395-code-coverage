from ..ifs.ex0 import ex0

import pytest

def test_ex0():
    assert ex0("abc", "def") == "def"

def test_ex0_equal():
    assert ex0("abc", "defg") == "defg"