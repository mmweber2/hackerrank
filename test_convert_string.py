from nose.tools import assert_equals
from convert_string import convert_string

def test_no_duplicates():
    assert_equals("xyz", convert_string("xyz"))

def test_all_duplicate_no_wrap():
    assert_equals("abc", convert_string("aaa"))

def test_all_duplicate_wrap():
    assert_equals("zab", convert_string("zzz"))
