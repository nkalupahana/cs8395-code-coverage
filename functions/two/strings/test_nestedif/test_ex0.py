from ..nestedif.ex0 import ex0

import pytest

def test_ex0():
    assert ex0('hello', 'world') == 'hello'
    assert ex0('HELLO', 'world') == 'world'

def test_ex0_with_up():
    assert ex0('hello', 'up') == 'HELLO'
    assert ex0('HELLO', 'up') == 'HELLO'

def test_ex0_with_down():
    assert ex0('hello', 'down') == 'hello'
    assert ex0('HELLO', 'down') == 'hello'