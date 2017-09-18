# Based on the HackerRank problem The Coin Change Problem:
# https://www.hackerrank.com/contests/programming-interview-questions/challenges/coin-change/copy-from/1303108984 

def get_ways_full(n, c):
    table = [[0] * (n + 1) for _ in xrange(len(c) + 1)]
    for i in xrange(len(c) + 1):
        # With any number of coins, there is 1 way to make 0 cents
        table[i][0] = 1
    # First row (no coins) is already filled in
    for row in xrange(1, len(c) + 1):
        for col in xrange(1, n + 1):
            coin = c[row-1]
            if col < coin:
                table[row][col] = table[row-1][col]
            else:
                table[row][col] = table[row-1][col] + table[row][col - coin]
    return table[-1][-1]

# Each row represents a coin, each column is a value of n
def get_ways(n, c):
    prev_row = [0] * (n + 1)
    # With any number of coins, there is 1 way to make 0 cents
    prev_row[0] = 1
    # Make current_row in scope to get the end result
    current_row = []
    # Fill len(c) rows
    for row in xrange(len(c)):
        current_row = [0] * (n + 1)
        current_row[0] = 1
        for col in xrange(1, n + 1):
            coin = c[row]
            if col < coin:
                current_row[col] = prev_row[col]
            else:
                current_row[col] = prev_row[col] + current_row[col - coin]
        prev_row = current_row
    return current_row[-1]

# Each column represents a coin, each row represents a value of n
def get_ways2(n, c):
    # If len(c) + 1, first column is no coins.
    # If len(c), first column is the first coin only.
    table = [[0] * (len(c) + 1) for _ in xrange(n + 1)]
    # With any number of coins, there is 1 way to make 0 cents
    table[0] = [1] * (len(c) + 1)
    for row in xrange(1, n + 1):
        # table[row][0] = 0: no way to make n > 0 with no coins
        for col in xrange(1, len(c) + 1):
            coin = c[col-1]
            if coin > row:
                table[row][col] = table[row][col-1]
            else:
                table[row][col] = table[row][col-1] + table[row-coin][col]
    return table[-1][-1]






# HackerRank version reads in from standard input, disabled for testing.
#n, m = map(int, raw_input().strip().split())
#c = map(long, raw_input().strip().split())
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
#get_ways(n, c)