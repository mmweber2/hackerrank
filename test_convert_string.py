from nose.tools import assert_equals
from convert_string import convert_string
from string import ascii_lowercase as letters

def test_no_duplicates():
    assert_equals("xyz", convert_string("xyz"))

def test_all_duplicate_no_wrap():
    assert_equals("abc", convert_string("aaa"))

def test_all_duplicate_wrap():
    assert_equals("zab", convert_string("zzz"))

def test_multiple_duplicates():
    assert_equals("ampbq", convert_string("ampap"))

def test_empty_string():
    assert_equals("", convert_string(""))

# Does an exact wrapping of 26 work?
def test_26_a():
    assert_equals(letters, convert_string("a" * 26))

def test_26_z():
    assert_equals("z" + letters[:25], convert_string("z" * 26))

# Does a wrapping of more than 26 work?
def test_27_a():
    assert_equals(letters + "a", convert_string("a" * 27))

def test_27_k():
    assert_equals("klmnopqrstuvwxyzabcdefghijk", convert_string("k" * 27))

# Does a wrapping of a multiple of 26 work?
def test_52_a():
    assert_equals(letters * 2 + "dogs", convert_string("a" * 52 + "dogs"))
