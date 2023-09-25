from functions.branch48 import branch48
import pytest

def test_branch48():
    assert branch48(0, 0, 0) == 0
    assert branch48(0, 0, 1) == 1
    assert branch48(0, 0, 2) == 2
    assert branch48(0, 0, 3) == 3
    assert branch48(0, 1, 0) == 1
    assert branch48(0, 1, 1) == 2
    assert branch48(0, 1, 2) == 3
    assert branch48(0, 1, 3) == 4
    assert branch48(0, 2, 0) == 2
    assert branch48(0, 2, 1) == 3
    assert branch48(0, 2, 2) == 4
    assert branch48(0, 2, 3) == 5
    assert branch48(0, 3, 0) == 3
    assert branch48(0, 3, 1) == 4
    assert branch48(0, 3, 2) == 5
    assert branch48(0, 3, 3) == 6
    assert branch48(1, 0, 0) == 1
    assert branch48(1, 0, 1) == 2
    assert branch48(1, 0, 2) == 3
    assert branch48(1, 0, 3) == 4
    assert branch48(1, 1, 0) == 2
    assert branch48(1, 1, 1) == 4
    assert branch48(1, 1, 2) == 6
    assert branch48(1, 1, 3) == 8
    assert branch48(1, 2, 0) == 3
    assert branch48(1, 2, 1) == 6
    assert branch48(1, 2, 2) == 9
    assert branch48(1, 2, 3) == 12
    assert branch48(1, 3, 0) == 4
    assert branch48(1, 3, 1) == 8
    assert branch48(1, 3, 2) == 12
    assert branch48(1, 3, 3) == 16
    assert branch48(2, 0, 0) == 2
    assert branch48(2, 0, 1) == 3
    assert branch48(2, 0, 2) == 4
    assert branch48(2, 0, 3) == 5
    assert branch48(2, 1, 0) == 3
    assert branch48(2, 1, 1) == 6
    assert branch48(2, 1, 2) == 9
    assert branch48(2, 1, 3) == 12
    assert branch48(2, 2, 0) == 4
    assert branch48(2, 2, 1) == 8
    assert branch48(2, 2, 2) == 12
    assert branch48(2, 2, 3) == 16
    assert branch48(2, 3, 0) == 5
    assert branch48(2, 3, 1) == 10
    assert branch48(2, 3, 2) == 15
    assert branch48(2, 3, 3) == 20
    assert branch48(3, 0, 0) == 3
    assert branch48(3, 0, 1) == 4
    assert branch48(3, 0, 2) == 5
    assert branch48(3, 0, 3) == 6
    assert branch48(3, 1, 0) == 4
    assert branch48(3, 1, 1) == 8
    assert branch48(3, 1, 2) == 12
    assert branch48(3, 1, 3) == 16
    assert branch48(3, 2, 0) == 5
    assert branch48(3, 2, 1) == 10
    assert branch48(3, 2, 2) == 15
    assert branch48(3, 2, 3) == 20
    assert branch48(3, 3, 0) == 6
    assert branch48(3, 3, 1) == 12
    assert branch48(3, 3, 2) == 18
    assert branch48(3, 3, 3) == 24