from ..ifelseif.ex8 import ex8

# Tests for ex8(num1, num2)

## Test Case 1: num1 > num2
def test_num1_greater_than_num2():
    assert ex8(5, 2) == 10

## Test Case 2: num2 > num1
def test_num2_greater_than_num1():
    assert ex8(2, 5) == 0.4

## Test Case 3: num1 == num2
def test_num1_equal_to_num2():
    assert ex8(3, 3) == 6