# Solution for HackerRank's Counter game
# https://www.hackerrank.com/challenges/counter-game

for _ in xrange(int(raw_input())):
    counter = int(raw_input())
    # If the initial value of the counter minus 1 has an odd number
    #     bits set, Louise (who plays first) will win the game,
    #     because it will take an even number of moves to reach 1 (the end state).
    print "Louise" if bin(counter - 1).count('1') & 1 else "Richard"

    # Example from the sample input:
    # Louise's turn: 6 (1010) => Richard's turn: 2 (10) =>
    # Louise's turn: 1, and she cannot make a move.

    # Another example:
    # Louise's turn: 20 (10100) => Richard's turn: 4 (100) =>
    # Louise's turn: 2 (10) => Richard's turn: 1, and he cannot make a move.
