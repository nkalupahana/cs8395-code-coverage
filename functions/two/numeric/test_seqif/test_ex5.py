from ..seqif.ex5 import ex5

# Test for ex5 function
def test_ex5_equal():
    assert ex5(5, 5) == 0

def test_ex5_greater():
    assert ex5(10, 5) == 5

def test_ex5_less():
    assert ex5(5, 10) == 5

def test_ex5_greater_than_10():
    assert ex5(20, 10) == 5

def test_ex5_less_than_10():
    assert ex5(10, 20) == 5

def test_ex5_negative():
    assert ex5(-5, -10) == 5

def test_ex5_negative_and_positive():
    assert ex5(-5, 10) == 15