# --- Day 4: The Ideal Stocking Stuffer ---

import hashlib

secret = input()

i , lead0 = 1, 5
while not hashlib.md5((secret + str(i)).encode()).hexdigest().startswith("0" * lead0): i += 1
print(i)

# --- Part Two ---

i, lead0 = 1, 6
while not hashlib.md5((secret + str(i)).encode()).hexdigest().startswith("0" * lead0): i += 1
print(i)
