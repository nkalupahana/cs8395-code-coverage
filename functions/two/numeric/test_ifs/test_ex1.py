from ..ifs.ex1 import ex1

# Import necessary modules
import pytest

# Define test cases
test_cases = [
    (5, 3, 8), # num1 > num2
    (3, 5, -2), # num1 < num2
    (0, 0, 0), # num1 = num2
    (-3, 5, 2), # num1 < 0
    (5, -3, 2), # num2 < 0
    (-3, -5, -8) # num1 < 0 and num2 < 0
]

# Define test function
def test_ex1():
    # Loop through test cases and assert equal results
    for num1, num2, expected in test_cases:
        assert ex1(num1, num2) == expected