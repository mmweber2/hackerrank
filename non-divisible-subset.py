# Solution for Hackerrank's Non-Divisible Subset
# https://www.hackerrank.com/challenges/non-divisible-subset

from collections import defaultdict

def get_len_subset(divisor, ints):
    # The size of the maximal subset (S')
    count = 0
    # In order for two numbers to have a sum not evenly divisible
    #    by k, the sum of each number % k must not equal k.
    # Therefore, we can find two numbers whose sum will not be divisible
    #    by k by choosing two numbers with mod values that do not sum to k.
    mods_to = defaultdict(int)
    for number in ints:
        mods_to[number % k] += 1
    if mods_to[0] > 0:
        # There exists a number in S that is evenly divisible by k,
        #   so it can be added to the set, but no other such numbers
        #   can be added.
        count = 1
    # Start at 1 because we already checked for a number x where (x % k = 0)
    for i in xrange(1, k / 2 + 1):
        # The number that could make a pair with i
        j = k - i
        if i == j and mods_to[i]:
            # There exists a number in S that mods to k / 2, and it can be added
            #    to the set, but no other such numbers can be added.
            # This is different from checking k / 2 because of integer division
            #    when k is an odd number.
            count += 1
        else:
            # Add all of the numbers that mod to i or mod to j to the subset,
            #    but not both
            count += max(mods_to[i], mods_to[j])
    print count

set_size, k = (int(x) for x in raw_input().split())
s = [int(y) for y in raw_input().split()]
get_len_subset(k, s)
