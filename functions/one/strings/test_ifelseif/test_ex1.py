from ..ifelseif.ex1 import ex1

import pytest

def test_empty_string():
  assert ex1('') == 'Empty string'

def test_single_character():
  assert ex1('a') == 'A'

def test_even_length_string():
  assert ex1('python') == 'pyTHON'

def test_odd_length_string():
  assert ex1('hello') == 'heLLO'