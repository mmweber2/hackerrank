# Solution for https://www.hackerrank.com/challenges/candies/problem

children = int(raw_input())
ratings = [int(raw_input()) for x in xrange(children)]
# Each child must get at least one candy
candies = [1] * children
for i in xrange(1, children):
    if ratings[i] > ratings[i-1]:
        # Higher rating than previous child; simply give one more candy
        candies[i] = candies[i-1] + 1
# The first pass can create an imbalance, so pass again to offset
# For example, where the ratings are 1 2 3 2 1, a single pass would
#   give extra candies to the first '2' and the '3' children,
#   but leave the second '2' child with only one candy.
for j in xrange(children - 2, -1, -1):
    if ratings[j] > ratings[j + 1] and candies[j] <= candies[j + 1]:
            candies[j] = candies[j + 1] + 1
# No children have candies at first, so the number of candies they have
#   at the end is the number that Alice gave them.
print sum(candies)
