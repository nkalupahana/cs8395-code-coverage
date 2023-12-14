from ..ifelseif.ex5 import ex5

import pytest

def test_ex5():
    # Test for string length greater than 10
    string = "abcdefghijklmnopqrstuvwxyz"
    assert ex5(string) == string.upper()
    
    # Test for string length between 5 and 10
    string = "hello world"
    assert ex5(string) == string.lower()
    
    # Test for string length less than or equal to 5
    string = "hello"
    assert ex5(string) == string.capitalize()
    
    # Test for empty string
    string = ""
    assert ex5(string) == string.capitalize()