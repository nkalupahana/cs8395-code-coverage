from ..ifs.ex6 import ex6

import pytest

def test_ex6():
    # Test case where num1 > num2
    assert ex6(5, 2) == 3
    
    # Test case where num2 > num1
    assert ex6(2, 5) == 3
    
    # Test case where num1 = num2
    assert ex6(5, 5) == 0