from ..none.ex4 import ex4

import pytest

def test_replace_spaces():
    # Test string with no spaces
    assert ex4("Hello_World") == "Hello_World"

    # Test string with one space
    assert ex4("Hello World") == "Hello_World"

    # Test string with multiple spaces
    assert ex4("Hello   World") == "Hello___World"

    # Test string with no spaces and special characters
    assert ex4("Hello$World") == "Hello$World"

    # Test string with only spaces
    assert ex4("   ") == "___"

    # Test empty string
    assert ex4("") == ""

    # Test string with leading and trailing spaces
    assert ex4(" Hello World ") == "_Hello_World_"

    # Test string with tabs
    assert ex4("Hello\tWorld") == "Hello_World"

    # Test string with newlines
    assert ex4("Hello\nWorld") == "Hello_World"