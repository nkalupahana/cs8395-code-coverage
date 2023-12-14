from ..ifelseif.ex2 import ex2

def test_ex2_equal_strings():
    assert ex2("Hello", "Hello") == "Hello"

def test_ex2_first_string_less_than_second():
    assert ex2("apple", "banana") == "applebanana"

def test_ex2_first_string_greater_than_second():
    assert ex2("zebra", "cat") == "catzebra"