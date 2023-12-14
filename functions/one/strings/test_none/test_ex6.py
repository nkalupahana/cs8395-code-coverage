from ..none.ex6 import ex6

import pytest

def test_ex6():
  assert ex6('hello') == 'olleh'
  assert ex6('racecar') == 'racecar'
  assert ex6('12345') == '54321'
  assert ex6('') == ''