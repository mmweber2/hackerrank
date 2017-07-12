# Solution for HackerRank's The Full Counting Sort
# https://www.hackerrank.com/challenges/countingsort4

# n may be up to one million, so use a defaultdict instead of a list
from collections import defaultdict

n = int(raw_input())
counts = defaultdict(list)
for i in xrange(n):
    num, s = raw_input().split()
    # The problem 'twist' is that any elements from the first half
    #    of the array should be printed as "-", so record them that
    #    way from the beginning.
    # Appending to a list keeps all values in their original order
    #    for each index.
    counts[int(num)].append("-") if i < n / 2 else counts[int(num)].append(s)
# Traverse counts (by keys) and concatenate all sublists.
for num in counts:
    print " ".join(counts[num]) ,