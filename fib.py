# Based on HackerRank problem Fibonacci Returns:
# https://www.hackerrank.com/contests/programming-interview-questions/challenges/fibonacci-returns/submissions/code/1303090357
# 

table = [0, 1]

def fib(n):
    '''Returns the nth zero-indexed fibonacci number.

    Raises IndexError if n < 0.

    Raises ValueError if n is not a valid integer. (Floats will be truncated to ints.)
    '''
    global table
    n = int(n)
    if n < 0:
        raise IndexError("n must be >= 0")
    if n < len(table):
        return table[n]
    while n >= len(table):
        new_sum = table[-1] + table[-2]
        table.append(new_sum)
    return table[-1]

# HackerRank version reads from STDIN and takes a single n on each line.
#while True:
#    try:
#        print fib(int(raw_input()))
#    except EOFError:
#        break
