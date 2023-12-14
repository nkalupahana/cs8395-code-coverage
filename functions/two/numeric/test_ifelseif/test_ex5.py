from ..ifelseif.ex5 import ex5

import pytest

def test_ex5():
    assert ex5(5, 10) == 5
    assert ex5(10, 5) == 5
    assert ex5(3, 3) == 9