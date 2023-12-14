from ..nestedif.ex6 import ex6

# test_ex6_1: test positive even number
def test_ex6_1():
  assert ex6(4) == 2

# test_ex6_2: test positive odd number
def test_ex6_2():
  assert ex6(5) == 15

# test_ex6_3: test zero
def test_ex6_3():
  assert ex6(0) == 0

# test_ex6_4: test negative number
def test_ex6_4():
  assert ex6(-3) == 0