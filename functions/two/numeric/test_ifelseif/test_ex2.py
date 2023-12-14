from ..ifelseif.ex2 import ex2

import pytest

def test_ex2_equal_numbers():
    assert ex2(3, 3) == 0

def test_ex2_first_num_greater():
    assert ex2(5, 3) == 2

def test_ex2_second_num_greater():
    assert ex2(3, 5) == 2