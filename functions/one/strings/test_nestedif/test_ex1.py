from ..nestedif.ex1 import ex1

import pytest

def test_ex1_long_string():
    string = 'This is a long string'
    assert ex1(string) == 'This is a long strings'

def test_ex1_short_string():
    string = 'short'
    assert ex1(string) == 'shorts'

def test_ex1_string_ends_with_s():
    string = 'Ends with s'
    assert ex1(string) == 'Ends with s'

def test_ex1_string_ends_with_other_letter():
    string = 'Ends with x'
    assert ex1(string) == 'Ends with xs'

def test_ex1_empty_string():
    string = ''
    assert ex1(string) == 's'