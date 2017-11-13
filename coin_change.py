# Based on the HackerRank problem The Coin Change Problem:
# https://www.hackerrank.com/contests/programming-interview-questions/challenges/coin-change/copy-from/1303108984 

# Each row represents a coin, each column is a value of n
def get_ways(n, coins):
    ways = [0] * (n + 1)
    # With any number of coins, there is 1 way to make 0 cents
    ways[0] = 1
    # Fill len(c) rows
    for coin in coins:
        # Start at coin, because the number of ways won't change
        #   for values smaller than the coin.
        for amt in xrange(coin, n + 1):
            ways[amt] += ways[amt-coin]
    return ways[-1]

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

