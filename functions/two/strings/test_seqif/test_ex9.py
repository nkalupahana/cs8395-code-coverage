from ..seqif.ex9 import ex9

import pytest

def test_ex9():
    assert ex9("hello", "world") == "HELLOworld"
    assert ex9("python", "code") == "pythoncode"
    assert ex9("testing", "TEST") == "TESTtest"