from ..ifelseif.ex0 import ex0

import pytest

def test_ex0():
    assert ex0(5) == 10
    assert ex0(15) == 20
    assert ex0(25) == 22
    assert ex0(10) == 10