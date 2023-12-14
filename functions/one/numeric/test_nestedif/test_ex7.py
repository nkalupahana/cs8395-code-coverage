from ..nestedif.ex7 import ex7

# Test for ex7 function

def test_ex7():
    assert ex7(5) == 5
    assert ex7(-5) == 2.5
    assert ex7(-15) == 7.5
    assert ex7(0) == 0
    assert ex7(10) == 10