from ..nestedif.ex7 import ex7

import pytest

# Test case for empty string
def test_ex7_empty():
    assert ex7("") == ""

# Test case for string starting with a vowel
def test_ex7_vowel():
    assert ex7("apple") == "appleway"

# Test case for string starting with a consonant
def test_ex7_consonant():
    assert ex7("banana") == "ananabay"

# Test case for string with multiple words
def test_ex7_multiple_words():
    assert ex7("hello world") == "ello worldhay"