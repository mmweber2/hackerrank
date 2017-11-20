# Solution for Hackerrank problem Triple Recursion.
# https://www.hackerrank.com/contests/w35/challenges/triple-recursion

if __name__ == "__main__":
    n, m, k = map(int, raw_input().strip().split(' '))
    # Given a square matrix of size n x n
    arr = [([0] * n) for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            if i == j:
                # Diagonal case
                if i == 0:
                    # Special case per problem statement
                    arr[i][j] = m
                else:
                    arr[i][j] = arr[i-1][j-1] + k
            elif i > j:
                arr[i][j] = arr[i-1][j] - 1
            else: # i < j
                arr[i][j] = arr[i][j-1] - 1
    # Print out the array with spaces and newlines, no commas or brackets
    print "\n".join(" ".join(str(x) for x in row) for row in arr)
