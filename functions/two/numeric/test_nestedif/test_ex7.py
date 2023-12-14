from ..nestedif.ex7 import ex7

import pytest

def test_ex7_num1_less_than_num2():
    num1 = 5
    num2 = 10
    assert ex7(num1, num2) == num1 / num2

def test_ex7_num1_greater_than_num2():
    num1 = 10
    num2 = 5
    assert ex7(num1, num2) == num1 * num2

def test_ex7_num2_zero():
    num1 = 5
    num2 = 0
    assert ex7(num1, num2) == 0