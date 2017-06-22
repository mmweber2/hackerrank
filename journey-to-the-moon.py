# Solution for HackerRank's Journey to the Moon
# https://www.hackerrank.com/challenges/journey-to-the-moon

num_astronauts, num_pairs = map(int, raw_input().split())
# Every astronaut belongs to their own country at first
graph = {i: set((i,)) for i in xrange(num_astronauts)}

# Read in the pair data and add each astronaut to the country
#     list of the other
for _ in xrange(num_pairs):
    a, b = map(int, raw_input().split())
    graph[a].add(b)
    graph[b].add(a)

# Group astronauts by country
countries = []
# Astronauts who have already been categorized
seen = set()
for i in xrange(num_astronauts):
    if i in seen:
        continue
     queue = [i]
     # Astronauts who share a country with this astronaut
     visited = set((i, ))
     while queue:
         current = queue.pop()
         new_people = [x for x in graph[current] if x not in visited]
         visited.update(new_people)
         queue.extend(new_people)
     countries.append(list(visited))
     seen.update(visited)

# We've grouped the astronauts by country, but we still need to identify how
#     many ways there are to pick two from two different countries.
ways = 0
previous_groups = 0

for j in xrange(len(countries)):
    group = countries[j]
    # Each astronaut can be paired with any astronaut not from the same country
    # Pair astronauts only with those from previously seen groups to avoid
    #    double counting
    ways += len(group) * previous_groups
    previous_groups += len(group)

print ways

