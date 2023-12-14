from ..none.ex0 import ex0

import pytest

@pytest.mark.parametrize('string, expected', [
  ('hello', 'ellohay'),
  ('python', 'ythonpay'),
  ('test', 'esttay'),
  ('', 'ay'),
  ('a', 'aay'),
])
def test_ex0(string, expected):
  assert ex0(string) == expected

def test_ex0_invalid_input():
  with pytest.raises(TypeError):
    ex0(123)