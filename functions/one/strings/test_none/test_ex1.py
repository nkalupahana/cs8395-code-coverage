from ..none.ex1 import ex1

import pytest

def test_ex1():
    string = "Hello World"
    assert ex1(string) == "hELLO wORLD"

def test_empty_string():
    string = ""
    assert ex1(string) == ""

def test_all_caps():
    string = "ALL CAPS"
    assert ex1(string) == "all caps"

def test_all_lower():
    string = "all lower"
    assert ex1(string) == "ALL LOWER"

def test_mixed_case():
    string = "MiXeD cAsE"
    assert ex1(string) == "mIxEd CaSe"