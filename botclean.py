# Solution for https://www.hackerrank.com/challenges/botclean
# This problem is a TSP, but a greedy solution is sufficient for
#   full points on this particular problem.

def next_move(posy, posx, board):
    if board[posy][posx] == 'd':
        return "CLEAN"
    adj_result = check_adjacent(posy, posx, board)
    if adj_result is not "NONE":
        return adj_result
    else:
        target_y, target_x = find_closest(posy, posx, board)
        if target_y > posy:
            return "DOWN"
        elif target_y < posy:
            return "UP"
        elif target_x > posx:
            return "RIGHT"
        elif target_x < posx:
            return "LEFT"
        # else: error case, but this is handled by the bot

def check_adjacent(posy, posx, board):
    # Check 4 adjacent squares
    if posx > 0 and board[posy][posx-1] == 'd':
        return "LEFT"
    if posx < 4 and board[posy][posx+1] == 'd':
        return "RIGHT"
    if posy > 0 and board[posy-1][posx] == 'd':
        return "UP"
    if posy < 4 and board[posy+1][posx] == 'd':
        return "DOWN"
    # Check diagonals; could do this the same time as the adjacent squares,
    #   but then we might move away from squares we're already adjacent to.
    if posx > 0:
        if ((posy > 0 and board[posy-1][posx-1] == 'd') or
            (posy < 4 and board[posy+1][posx-1] == 'd')):
            # Will move up or down on the next move when the dirty square
            # is found to be adjacent to the new position
            return "LEFT"
    if posx < 4:
        if ((posy > 0 and board[posy-1][posx+1] == 'd') or
            (posy < 4 and board[posy+1][posx+1] == 'd')):
            return "RIGHT"
    # Error case; return a string for type consistency
    return "NONE"

def find_closest(posy, posx, board):
    min_dist = float('inf')
    # If the current position is dirty, it will always be cleaned
    #   before any search is attempted.
    closest = (posy, posx)
    for y in xrange(5):
        for x in xrange(5):
            if board[y][x] != 'd' or (y, x) == closest:
                    continue
            # Get Euclidean distance to each dirty square
            if posx == x:
                # Avoid dividing by zero when dirty spot is in the same column
                dist = float(abs(posy - y))
            else:
                dist = float(abs(posy - y)) / float(abs(posx - x))
            if dist < min_dist:
                min_dist = dist
                closest = (y, x)
    return closest

# I don't have access to the HackerRank bot itself, so I manually entered
#    the board data and had it keep track of its current position, as well as
#    the number of dirty spots remaining on the board.
board = ['-d---', '-d---', '---d-', '---d-', '--d-d']
dirty_count = 0
for y in xrange(5):
    for x in xrange(5):
        if board[y][x] == 'd':
            dirty_count += 1
# Bot always starts in the upper left corner of the grid
posy, posx = 0, 0

while dirty_count:
    move = next_move(posy, posx, board)
    print move
    if move == "CLEAN":
        if board[posy][posx] != 'd':
            # The HackerRank bot handles this error checking.
            raise IndexError("Not dirty at {}, {}!".format(posy, posx))
        # I represented the rows with strings for readability, but if they
        #     were lists, I could just change the char at this index.
        board[posy] = board[posy][:posx] + '-' + board[posy][posx+1:]
        dirty_count -= 1
    elif move == "UP":
       posy -= 1
    elif move == "DOWN":
       posy += 1
    elif move == "RIGHT":
       posx += 1
    elif move == "LEFT":
       posx -= 1
    # else: Error case, handled by the HackerRank bot
