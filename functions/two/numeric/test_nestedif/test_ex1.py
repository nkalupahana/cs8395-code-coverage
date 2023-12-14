from ..nestedif.ex1 import ex1

import pytest

# test case for when a > b and result < 10
def test_ex1_case1():
    assert ex1(15, 10) == 10

# test case for when a > b and result > 10
def test_ex1_case2():
    assert ex1(20, 10) == 15

# test case for when a < b and result > 10
def test_ex1_case3():
    assert ex1(10, 20) == 5

# test case for when a < b and result < 10
def test_ex1_case4():
    assert ex1(5, 10) == 10