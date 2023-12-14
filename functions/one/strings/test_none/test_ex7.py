from ..none.ex7 import ex7

def test_ex7():
    assert ex7("hello") == "olleh"
    
def test_ex7_empty():
    assert ex7("") == ""
    
def test_ex7_single_char():
    assert ex7("a") == "a"
    
def test_ex7_long_string():
    assert ex7("abcdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedcba"