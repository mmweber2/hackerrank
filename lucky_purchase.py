# Code for Hackerrank challenge "Lucky Purchase".
# https://www.hackerrank.com/contests/w35/challenges/lucky-purchase

if __name__ == "__main__":
    n = int(raw_input().strip())
    laptops = []
    for _ in xrange(n):
        name, value = raw_input().strip().split(' ')
        four_count = value.count('4')
        # Don't consider this laptop if it has no 4s in its price
        if not four_count: continue
        seven_count = value.count('7')
        # Don't consider this laptop if it doesn't have an equal number
        #      of 4 and 7 in its price
        if seven_count != four_count: continue
        if four_count * seven_count == len(value):
            # Only consider laptops with no other digits in the price
            laptops.append((int(value), name))
    if not laptops:
        print -1
    else:
        laptops.sort()
        # The first laptop will be the cheapest one that meets these conditions
        print laptops[0][1]
