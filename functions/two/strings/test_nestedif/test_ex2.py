from ..nestedif.ex2 import ex2

# Test case 1: len(string1) > len(string2)
def test_ex2_long_string():
    assert ex2("hello", "world") == "HELLOWORLD"

# Test case 2: len(string1) < len(string2)
def test_ex2_short_string():
    assert ex2("hey", "there") == "heythere"

# Test case 3: len(combo_string) > 10
def test_ex2_long_combo():
    assert ex2("python", "isawesome") == "PYTHONISAWESOME"

# Test case 4: len(combo_string) < 10
def test_ex2_short_combo():
    assert ex2("hi", "there") == "hithere"

# Test case 5: len(string1) = len(string2)
def test_ex2_equal_strings():
    assert ex2("hello", "hello") == "hellohello"