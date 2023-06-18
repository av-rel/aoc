# --- Day 8: Matchsticks ---

strings = open(0).read().splitlines()

print(sum(len(s) - len(eval(s)) for s in strings))

# --- Part Two ---
print(sum(s.count('"') + s.count('\\') + 2 for s in strings))
