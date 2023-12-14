from ..seqif.ex3 import ex3

import pytest

def test_ex3_longer_string():
    string1 = "hello"
    string2 = "world"
    assert ex3(string1, string2) == "helloworld"

def test_ex3_shorter_string():
    string1 = "hello"
    string2 = "world"
    assert ex3(string2, string1) == "worldhello"

def test_ex3_string1_empty():
    string1 = ""
    string2 = "world"
    assert ex3(string1, string2) == "world"

def test_ex3_string2_empty():
    string1 = "hello"
    string2 = ""
    assert ex3(string1, string2) == "hello"

def test_ex3_both_strings_empty():
    string1 = ""
    string2 = ""
    assert ex3(string1, string2) == ""

def test_ex3_string1_longer_than_string2():
    string1 = "hello"
    string2 = "world"
    assert ex3(string1, string2) == "helloworld"

def test_ex3_string2_longer_than_string1():
    string1 = "world"
    string2 = "hello"
    assert ex3(string1, string2) == "worldhello"

def test_ex3_string1_contains_AB():
    string1 = "ABCD"
    string2 = "EFGH"
    assert ex3(string1, string2) == "CDABEFGH"

def test_ex3_string2_contains_AB():
    string1 = "EFGH"
    string2 = "ABCD"
    assert ex3(string1, string2) == "CDABEFGH"

def test_ex3_both_strings_contain_AB():
    string1 = "ABCD"
    string2 = "EFGHAB"
    assert ex3(string1, string2) == "CDEFGH"