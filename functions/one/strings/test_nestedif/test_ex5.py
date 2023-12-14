from ..nestedif.ex5 import ex5

# Test for string with length >= 10
def test_ex5_long_string():
    assert ex5("HELLO WORLD") == "hello world"
    
# Test for string with length < 10
def test_ex5_short_string():
    assert ex5("hello") == "hello"
    
# Test for string with length >= 10 and all uppercase
def test_ex5_all_upper():
    assert ex5("HELLO") == "hello"
    
# Test for string with length >= 10 and all lowercase
def test_ex5_all_lower():
    assert ex5("hello") == "HELLO"
    
# Test for empty string
def test_ex5_empty_string():
    assert ex5("") == ""