from ..none.ex2 import ex2

import pytest

# Test Case 1
def test_ex2_case1():
    assert ex2("Hello", "World") == "HELLOworld"

# Test Case 2
def test_ex2_case2():
    assert ex2("python", "TESTING") == "PYTHONtesting"

# Test Case 3
def test_ex2_case3():
    assert ex2("code", "COVERAGE") == "CODEcoverage"

# Test Case 4
def test_ex2_case4():
    assert ex2("100%", "CODE COVERAGE") == "100%code coverage"

# Test Case 5
def test_ex2_case5():
    assert ex2("Hello", "") == "HELLO"

# Test Case 6
def test_ex2_case6():
    assert ex2("", "world") == "world"