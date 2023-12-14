from ..ifelseif.ex7 import ex7

import pytest

def test_ex7():
    # Test case 1: arg1 > arg2
    assert ex7(5, 3) == 2

    # Test case 2: arg1 < arg2
    assert ex7(3, 5) == 2

    # Test case 3: arg1 = arg2
    assert ex7(5, 5) == 10