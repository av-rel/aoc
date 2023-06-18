# --- Day 10: Elves Look, Elves Say ---

digits = input()

def solve(text, n) -> str:
    if n == 0: return text
    con = ''
    i = 0
    while i < len(text):
        alp = text[i]
        i += 1
        while i < len(text) and alp[0] == text[i]:
            alp += text[i]
            i += 1
        con += str(len(alp)) + alp[0]

    return solve(con, n-1)

print(len(solve(digits, 40)))

# --- Part Two ---

print(len(solve(digits, 50)))
