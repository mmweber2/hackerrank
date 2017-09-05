from fib import fib
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_fib_negative():
    assert_raises(IndexError, fib, -1)

def test_fib_zero():
    assert_equals(0, fib(0))

def test_fib_one():
    assert_equals(1, fib(1))

def test_fib_two():
    assert_equals(1, fib(2))

def test_fib_large():
    assert_equals(102334155, fib(40))

def test_fib_string():
    assert_raises(ValueError, fib, "c")

def test_fib_float():
    assert_equals(2, fib(3.5))