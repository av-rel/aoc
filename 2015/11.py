# --- Day 11: Corporate Policy ---

password = input()
sequence = lambda st: any(ord(a) + 2 == ord(b) + 1 == ord(c) for a, b, c in zip(st, st[1:], st[2:]))
doublets = lambda st: len(set(a for a, b in zip(st, st[1:]) if a == b)) > 1

def santa_encrypt(text) -> str:
    encrypted = False
    while not encrypted:
        text = text.rstrip("z")
        if text:
            i, char = next(((i, c) for i, c in enumerate(text) if c in "ilo"), (-1, text[-1]))
            text = text[0:i] + ("jmp"[q] if (q := "hkn".find(char)) != -1 else chr(ord(char) + 1))
        text = text.ljust(8, "a")
        if sequence(text) and doublets(text): encrypted = True

    return text

print(new_pass := santa_encrypt(password))

# --- Part Two ---

print(santa_encrypt(new_pass))
