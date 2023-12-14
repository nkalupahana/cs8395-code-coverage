from ..none.ex2 import ex2

# Tests for ex2

# Test Case 1: Empty String
def test_ex2_empty():
    assert ex2("") == ""

# Test Case 2: Single Character String
def test_ex2_single_char():
    assert ex2("a") == "A"

# Test Case 3: All Lowercase String
def test_ex2_all_lowercase():
    assert ex2("abcdefg") == "GFEDCBA"

# Test Case 4: All Uppercase String
def test_ex2_all_uppercase():
    assert ex2("ABCDEFG") == "GFEDCBA"

# Test Case 5: Mixed Case String
def test_ex2_mixed_case():
    assert ex2("AbCdEfG") == "GFEDCBA"

# Test Case 6: String with Spaces
def test_ex2_spaces():
    assert ex2("a b c d e f g") == "GFEDCBA"

# Test Case 7: String with Special Characters
def test_ex2_special_char():
    assert ex2("!@#$%^&*()") == ")(*&^%$#@!"

# Test Case 8: String with Numbers
def test_ex2_numbers():
    assert ex2("123456789") == "987654321"