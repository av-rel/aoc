# --- Day 5: Doesn't He Have Intern-Elves For This? ---

strings = open(0).readlines()
nice : list[str] = []
noc = list = [('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y')]

for st in strings:
    vc = 0
    sc = 0
    nc = 0
    for v in 'aeiou':
        vc += st.count(v)
    for i, s in enumerate(st):
        if len(st) > i + 1 and st[i+1] == s:
            sc += 1
        if len(st) > i + 1:
            a, b = s, st[i+1]
            if (a, b) in noc:
                nc += 1
    
    if vc >= 3 and sc >= 1 and nc == 0:
        nice.append(st)

print(len(nice))

# --- Part Two ---

nice = []

for st in strings:
    r1 = 0
    r2 = 0

    for i, s in enumerate(st):
        if len(st) > i + 1 and st.count(s + st[i+1]) == 2:
            r1 += 1
    
        if len(st) > i + 2:
            a, _, c = s, st[i+1], st[i+2]
            if a == c:
                r2 += 1

    if r1 >= 2 and r2 >= 1:
        nice.append(st)
 
print(len(nice))
