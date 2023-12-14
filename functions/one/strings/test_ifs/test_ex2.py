from ..ifs.ex2 import ex2

# test_ex2.py
def test_ex2_less_than_five():
    assert ex2("hello") == "hello"

def test_ex2_equal_to_five():
    assert ex2("world") == "world"

def test_ex2_greater_than_five():
    assert ex2("python") == "pytho"