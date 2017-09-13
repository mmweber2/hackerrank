# From HackerRank problem Bonetrousle
# https://www.hackerrank.com/challenges/bonetrousle/problem

# n = sticks, k = boxes for sale, b = boxes to buy
def get_boxes(n, k, b):
    # Sum of first b numbers (buy the b smallest boxes)
    min_total = b * (b + 1)/2
    smallest_boxes = k - b
    # Sum of last b numbers (buy the b largest boxes)
    max_total = k * (k + 1)/2 - (smallest_boxes * (smallest_boxes + 1))/2
    if not (min_total <= n <= max_total):
        return "-1"
    # Buy the first b boxes, then add the difference
    #    between the desired and minimum totals across the boxes
    boxes_bought = [x + (n - min_total)/b for x in xrange(1, b + 1)]
    # Since the excess might not divide evenly, apply the remainder
    #    across the boxes
    remainder = (n - min_total) % b
    # Apply the remainder to the end, because we started with the first b
    for i in xrange(b-1, b - remainder - 1, -1):
        boxes_bought[i] += 1
    return " ".join(str(x) for x in boxes_bought)
    
for _ in xrange(int(raw_input().strip())):
    n, k, b = (int(x) for x in raw_input().strip().split())
    print get_boxes(n, k, b)