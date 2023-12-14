from ..ifs.ex9 import ex9

import pytest

def test_ex9():
    assert ex9("hello", "world") == "worldhello"
    assert ex9("python", "code") == "pythoncode"
    assert ex9("test", "pytest") == "pytesttest"
    assert ex9("abc", "defg") == "defgabc"
    assert ex9("longer", "short") == "longershort"
    
def test_ex9_same_length():
    assert ex9("apple", "banana") == "applebanana"
    assert ex9("cat", "dog") == "dogcat"
    assert ex9("python", "java") == "javapython"
    assert ex9("good", "better") == "bettergood"
    assert ex9("hello", "world") == "worldhello"