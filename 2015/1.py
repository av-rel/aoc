# --- Day 1: Not Quite Lisp ---

parens = input()

floor = 0

for paren in parens:
    if paren == '(':
        floor += 1
    elif paren == ')':
        floor -= 1

print(floor)

# --- Part Two ---

floor = 0

for i, paren in enumerate(parens):
    if paren == '(':
        floor += 1
    elif paren == ')':
        floor -= 1

    if floor == -1:
        floor = i + 1
        break

print(floor)
