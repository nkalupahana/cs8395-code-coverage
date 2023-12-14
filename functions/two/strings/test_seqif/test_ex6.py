from ..seqif.ex6 import ex6

# Import the necessary modules
import pytest

# Define a function to test the ex6 function
def test_ex6():
    # Test case 1: combined string is longer than 10 characters
    assert ex6("hello", "world") == "dlrowolleh"
    
    # Test case 2: combined string is shorter than or equal to 10 characters
    assert ex6("good", "morning") == "GOODMORNING"