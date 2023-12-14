from ..ifs.ex7 import ex7

import pytest

def test_ex7():
    assert ex7(5, 3) == 2
    assert ex7(3, 5) == 8