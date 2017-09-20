# From HackerRank problem Lily's Homework
# https://www.hackerrank.com/challenges/lilys-homework/problem

n = int(raw_input().strip())
a = map(int, raw_input().strip().split())

def count_swaps(input_list):
    # Track the current indices of every number
    # Per the problem statement, all numbers are distinct
    positions = {}
    for i in xrange(len(input_list)):
        positions[input_list[i]] = i
    s_list = sorted(input_list)
    swaps = 0
    for i in xrange(len(input_list)):
        current = input_list[i]
        sorted_val = s_list[i]
        if current != sorted_val:
            swaps += 1
            # The current number belongs where the sorted number used to be
            positions[current] = positions[sorted_val]
            # Swap the two numbers
            input_list[i], input_list[positions[sorted_val]] = sorted_val, current
    return swaps
        
# Compare the number of swaps for ascending and descending order,
#   because they are both equally beautiful per the problem statement
# The process modifies the array, so check the reverse copy first.
# (To avoid modifying the array, use a separate copy for each call to count_swaps.)
print min(count_swaps(a[::-1]), count_swaps(a))