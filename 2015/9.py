# --- Day 9: All in a Single Night ---

import collections, itertools

dists = collections.defaultdict(dict)
for ln in open(0).read().splitlines():
    start, _, end, _, time = ln.split()
    dists[start][end] = dists[end][start] = int(time)
routes = [sum(dists[src][dst] for src, dst in itertools.pairwise(p)) for p in itertools.permutations(dists.keys())]

print(min(routes))

# --- Part Two ---

print(max(routes))
