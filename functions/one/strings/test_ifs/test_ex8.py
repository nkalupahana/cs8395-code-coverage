from ..ifs.ex8 import ex8

# Test for string length greater than 5
def test_ex8_upper():
    assert ex8("Hello") == "HELLO"

# Test for string length less than or equal to 5
def test_ex8_lower():
    assert ex8("Hi") == "hi"