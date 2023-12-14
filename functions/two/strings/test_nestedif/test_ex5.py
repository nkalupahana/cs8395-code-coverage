from ..nestedif.ex5 import ex5

import pytest

def test_ex5():
    assert ex5('abc', 'def') == 'abcdef'
    assert ex5('hello', 'world') == 'worldhello'
    assert ex5('python', 'language') == 'languagepython'
    assert ex5('a', 'b') == 'ba'
    assert ex5('xyz', '123') == '123xyz'