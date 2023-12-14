from ..nestedif.ex3 import ex3

import pytest

def test_ex3_length_greater_than_5():
    # Arrange
    string = "apple"

    # Act
    result = ex3(string)

    # Assert
    assert result == "EPPLE"

def test_ex3_length_less_than_5():
    # Arrange
    string = "cat"

    # Act
    result = ex3(string)

    # Assert
    assert result == "cat"

def test_ex3_lowercase():
    # Arrange
    string = "banana"

    # Act
    result = ex3(string)

    # Assert
    assert result == "bEnEnE"

def test_ex3_uppercase():
    # Arrange
    string = "ORANGE"

    # Act
    result = ex3(string)

    # Assert
    assert result == "ORANGE"