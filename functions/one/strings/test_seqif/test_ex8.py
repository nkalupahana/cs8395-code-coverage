from ..seqif.ex8 import ex8

# test_ex8_long_string
def test_ex8_long_string():
    assert ex8("This is a long string") == "This is a long string is long!"

# test_ex8_short_string
def test_ex8_short_string():
    assert ex8("Short string") == "Short string is short!"

# test_ex8_empty_string
def test_ex8_empty_string():
    assert ex8("") == " is short!"