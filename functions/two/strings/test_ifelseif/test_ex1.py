from ..ifelseif.ex1 import ex1

import pytest

def test_ex1_same_strings():
    assert ex1("hello", "hello") == "The strings are the same."

def test_ex1_first_longer():
    assert ex1("hello", "hi") == "The first string is longer than the second by 3 characters."

def test_ex1_second_longer():
    assert ex1("hi", "hello") == "The second string is longer than the first by 3 characters."

def test_ex1_empty_strings():
    assert ex1("", "") == "The strings are the same."

def test_ex1_different_length():
    assert ex1("hi", "hello") == "The second string is longer than the first by 2 characters."

def test_ex1_whitespace_strings():
    assert ex1(" ", "  ") == "The first string is longer than the second by 1 characters."