from ..seqif.ex0 import ex0

import pytest

def test_ex0():
    assert ex0(5) == 4
    assert ex0(10) == 9
    assert ex0(11) == 16