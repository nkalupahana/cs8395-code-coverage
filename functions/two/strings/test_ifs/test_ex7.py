from ..ifs.ex7 import ex7

# test_ex7
import pytest

def test_ex7_same_length():
    # Arrange
    string1 = "abc"
    string2 = "def"

    # Act
    result = ex7(string1, string2)

    # Assert
    assert result == "abcdef"

def test_ex7_string1_longer():
    # Arrange
    string1 = "longer string"
    string2 = "short"

    # Act
    result = ex7(string1, string2)

    # Assert
    assert result == "longer stringshort"

def test_ex7_string2_longer():
    # Arrange
    string1 = "short"
    string2 = "longer string"

    # Act
    result = ex7(string1, string2)

    # Assert
    assert result == "longer stringshort"