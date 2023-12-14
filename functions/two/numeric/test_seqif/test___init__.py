from ..seqif.__init__ import __init__

# Example function:

def add(x, y):
    return x + y

# Generated tests:

import pytest

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 5) == 4
    assert add(10, -10) == 0
    assert add(2, 3) == 5
    assert add(-5, -5) == -10