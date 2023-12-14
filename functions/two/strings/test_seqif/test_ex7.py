from ..seqif.ex7 import ex7

import pytest

def test_longer_string_first():
    assert ex7('hello', 'hi') == 'hellohi'

def test_longer_string_second():
    assert ex7('hi', 'hello') == 'hellohi'

def test_replace_a_with_b():
    assert ex7('hello', 'hi') == 'hbllobhi'
    assert ex7('hi', 'hello') == 'hbllohi'