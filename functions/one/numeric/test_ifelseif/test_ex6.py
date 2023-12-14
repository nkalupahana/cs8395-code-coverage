from ..ifelseif.ex6 import ex6

import pytest

def test_ex6():
    assert ex6(-10) == 0
    assert ex6(5) == 6
    assert ex6(10) == 20