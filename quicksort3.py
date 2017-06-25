# Solution for Hackerrank's Quicksort In-Place
# https://www.hackerrank.com/challenges/quicksort3/problem

def quicksort(array, start=0, end=None):
    if end is None:
        # Initial function call
        end = len(array) - 1
    if start >= end:
        # Nothing left to sort
        return
    # The sorted position of the pivot
    pivot_pos = partition(array, start, end)
    # Sort both halves of the array recursively
    quicksort(array, start, pivot_pos - 1)
    quicksort(array, pivot_pos + 1, end)

def partition(array, start, end):
    # Lomuto partition algorithm
    pivot = array[end]
    # Correct position of the pivot
    swap_pos = start
    for i in xrange(start, end):
        if array[i] <= pivot:
            # Update the end position of the pivot by tracking how many
            #     items in the array are smaller than or equal to it
            array[i], array[swap] = array[swap], array[i]
            swap += 1
    # Move the pivot to its correct position
    array[end], array[swap] = array[swap], array[end]
    return swap

n = raw_input()
quicksort(map(int, sys.stdin.readline().strip().split()))
