from coin_change import get_ways
from nose.tools import assert_equals

# Problem constraints:
# 1 <= c[i] <= 50
# 1 <= n <= 250
# 1 <= m <= 50
# Each c[i] is guaranteed to be distinct.
#

def test_cannot_reach_1():
    assert_equals(0, get_ways(1, [2, 3]))

def test_unreachable():
    assert_equals(0, get_ways(4, [3]))

def test_large_coin():
    assert_equals(0, get_ways(5, [50]))

def test_reach_first_coin():
    assert_equals(1, get_ways(1, [1, 2]))

def test_reach_later_coin():
    assert_equals(1, get_ways(5, [2, 4, 5]))

def test_multiple_coins():
    assert_equals(1, get_ways(5, [2, 3]))

def test_multiples_single_coin():
    assert_equals(1, get_ways(3, [1, 5]))

def test_multiple_ways():
    assert_equals(3, get_ways(3, [8, 1, 3, 2]))