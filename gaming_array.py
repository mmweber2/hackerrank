# HackerRank problem: Gaming Array
# https://www.hackerrank.com/challenges/an-interesting-game-1

def print_winner():
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split())
    # Is Bob winning?
    bob = True # Given that n >= 1, so Bob can always make a move
    curr_max = arr[0]
    for i in xrange(1, n):
        if arr[i] > curr_max:
            # If the number of new maxes (moving from left to right) in the
            #   array is odd, Bob wins. Otherwise, Andy wins.
            bob ^= True
            curr_max = arr[i]
    print "BOB" if bob else "ANDY"

games = int(raw_input().strip())
for _ in xrange(games):
    print_winner()
