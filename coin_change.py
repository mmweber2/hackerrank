# Based on the HackerRank problem The Coin Change Problem:
# https://www.hackerrank.com/contests/programming-interview-questions/challenges/coin-change/copy-from/1303108984 

def get_ways(n, c):
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


# HackerRank version reads in from standard input, disabled for testing.
#n, m = map(int, raw_input().strip().split())
#c = map(long, raw_input().strip().split())
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
#get_ways(n, c)