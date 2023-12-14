from ..ifs.ex5 import ex5

# Test for ex5 function
def test_ex5():
    # Test case 1
    assert ex5(5, 3) == 2

    # Test case 2
    assert ex5(10, 15) == 5

    # Test case 3
    assert ex5(-3, 7) == 10

    # Test case 4
    assert ex5(0, 0) == 0

    # Test case 5
    assert ex5(-5, -10) == 5