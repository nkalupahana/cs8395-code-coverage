from ..nestedif.ex9 import ex9

# tests for ex9 function
import pytest

# test case for num > 50
def test_ex9_greater_than_50():
    assert ex9(60) == 140

# test case for num < 50
def test_ex9_less_than_50():
    assert ex9(40) == 40

# test case for num < 50 and num < 100
def test_ex9_less_than_100():
    assert ex9(80) == 160

# test case for num > 100
def test_ex9_greater_than_100():
    assert ex9(110) == 110