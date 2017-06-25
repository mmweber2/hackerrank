# Solution for Hackerrank's Sherlock and Anagrams:
# https://www.hackerrank.com/challenges/sherlock-and-anagrams

from collections import defaultdict

def count_pairs(s):
    # Track occurrences of normalized versions of each substring
    counts = defaultdict(int)
    for start in xrange(len(s)):
        for end in xrange(start + 1, len(s) + 1):
            # Make substring of start to end, then sort it to normalize
            #    anagrams to the same string.
            counts["".join(sorted(s[start:end]))] += 1
    # If a substring anagram was seen more than once, we can form pairs
    #     with the other substrings of that anagram.
    # Divide by two because we are looking for unordered pairs.
    return sum(x * (x - 1) / 2 for x in counts.values() if x > 1)

 num_cases = int(raw_input())
 for _ in xrange(num_tests):
     print count_pairs(raw_input().strip())
