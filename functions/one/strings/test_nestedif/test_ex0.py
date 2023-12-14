from ..nestedif.ex0 import ex0

# Generated test cases for ex0 function

## Test case 1: string length is less than 5, no '!' in string
def test_ex0_case1():
    assert ex0("") == ""

## Test case 2: string length is 5, no '!' in string
def test_ex0_case2():
    assert ex0("hello") == "hello"

## Test case 3: string length is greater than 5, no '!' in string
def test_ex0_case3():
    assert ex0("hello world") == "hello world"

## Test case 4: string length is less than 5, '!' in string
def test_ex0_case4():
    assert ex0("hi!") == "hi!"

## Test case 5: string length is 5, '!' in string
def test_ex0_case5():
    assert ex0("hello!") == "hello?"

## Test case 6: string length is greater than 5, '!' in string
def test_ex0_case6():
    assert ex0("hello world!") == "hello world?"