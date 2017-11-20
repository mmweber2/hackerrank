# Solution for Hackerrank problem 3D Surface Area
# https://www.hackerrank.com/contests/w35/challenges/3d-surface-area

def surface_area(cubes):
    total_area = sum(cubes[0]) # Start with area from the front
    for i in xrange(len(cubes)):
        row = cubes[i]
        # Already handled the first row's (i=0) front,
        #      but not the other cases for i = 0
        if i:
            # Each position in this row will be shorter than, taller than,
            #    or the same height as the position in the previous row.
            # Any difference in height means exposed surface area.
            height_diffs = (abs(cubes[i][x] - cubes[i-1][x]) for x in xrange(len(row)))
            total_area += sum(height_diffs)
        # Add area from sides
        # Always add the outer edges, since they're never blocked
        total_area += row[0] + row[-1]
        # Area from left to right
        for j in xrange(len(row)):
            # Like the comparison to previous rows, we need to compare
            #    to adjacent spaces within the same row, but can't use
            #    the same syntax because of indexing errors.
            if j > 0 and row[j] > row[j-1]:
                total_area += row[j] - row[j-1]
            if j < len(row) - 1 and row[j] > row[j+1]:
                total_area += row[j] - row[j+1]
    # Add area of back
    return total_area + sum(cubes[-1])

if __name__ == "__main__":
    H, W = map(int, raw_input().strip().split(' '))
    cubes = [map(int, raw_input().strip().split()) for _ in xrange(H)]
    # It is given that every area has at least one cube,
    #     so the top and bottom area are each H * W.
    # Add them here where we have access to H and W.
    print surface_area(cubes) + (H * W * 2)
