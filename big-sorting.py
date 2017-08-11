# Solution for https://www.hackerrank.com/challenges/big-sorting

n = int(raw_input().strip())
# Due to the large input size (up to 2 * 10**5 numbers), converting
#    the keys to integers while reading them in caused a timeout.
unsorted = (raw_input() for _ in xrange(n))
# Exploit Python's natural handling of large numbers
for num in sorted(unsorted, key=int):
    print num