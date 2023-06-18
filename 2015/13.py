# --- Day 13: Knights of the Dinner Table ---

import collections, itertools

fl = open(0)
dt = collections.defaultdict(lambda: collections.defaultdict(int))
total = lambda perm: sum(dt[a][b] + dt[b][a] for a, b in itertools.pairwise(perm + (perm[0],)))

def solve(me) -> int:
    for line in fl:
        name, _, op, n, *_, dst = line.split()
        dt[name][dst[:-1]] = int(n) * (1 if op == "gain" else -1)
    return max(total(perm) for perm in itertools.permutations(tuple(dt.keys()) + me))

print(solve(()))

# --- Part Two ---

print(solve(("self",)))
