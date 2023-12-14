from ..nestedif.ex4 import ex4

import pytest

# Test that function returns correct result when first string is longer than second string and the first string contains the second string
def test_first_longer_contains():
    assert ex4('hello', 'he') == 'llo'

# Test that function returns correct result when first string is longer than second string and the first string does not contain the second string
def test_first_longer_not_contains():
    assert ex4('hello', 'hi') == 'hellohi'

# Test that function returns correct result when first string is equal in length to second string
def test_equal_length():
    assert ex4('hello', 'hell') == 'o'

# Test that function returns correct result when first string is shorter than second string
def test_first_shorter():
    assert ex4('hi', 'hello') == 'hihello'

# Test that function returns correct result when first string is empty
def test_first_empty():
    assert ex4('', 'hello') == 'hello'

# Test that function returns correct result when second string is empty
def test_second_empty():
    assert ex4('hello', '') == 'hello'