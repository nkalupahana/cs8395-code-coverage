from ..ifelseif.ex8 import ex8

import pytest

def test_ex8_replace_a():
    assert ex8('abc') == 'bbc'

def test_ex8_replace_b():
    assert ex8('bca') == 'cca'

def test_ex8_replace_c():
    assert ex8('cab') == 'aab'

def test_ex8_no_replace():
    assert ex8('def') == 'def'