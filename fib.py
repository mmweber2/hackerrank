def fib(n):
    '''Returns the nth zero-indexed fibonacci number.

    Raises IndexError if n < 0.
    '''
    global table
    if n < 0:
        raise IndexError("n must be >= 0")
    if n < len(table):
        return table[n]
    while n >= len(table):
        new_sum = table[-1] + table[-2]
        table.append(new_sum)
    return table[-1]

table = [0, 1]
# HackerRank version read from STDIN
while True:
    try:
        print fib(int(raw_input()))
    except EOFError:
        break
