# --- Day 6: Probably a Fire Hazard ---

import itertools

lines = open(0).readlines()
stride = 1000
grid = [[0] * stride for _ in range(stride)]

def action(inst : str, state : int, ane : int = 0) -> int:
    if inst == "toggle":
        if ane == 0:
            state = not state
        else:
            state = state + 2
    elif inst == "on":
        if ane == 0:
            state = 1
        else:
            state = state + 1
    elif inst == "off":
        if ane == 0:
            state = 0
        else:
            state = max(state - 1, 0)
    return state

inst = ""
(x1, y1), (x2, y2) = (0, 0), (0, 0)

def stabel(ln):
    global inst
    global x1, y1, x2, y2

    c = ln.split(" ")
    inst = c[0]
    cord_0 = c[1].split(',')
    cord_1 = c[3].split(',')

    if inst == "turn":
        inst = c[1]
        cord_0 = c[2].split(',')
        cord_1 = c[4].split(',')
    
    x1, y1 = int(cord_0[0]), int(cord_0[1])
    x2, y2 = int(cord_1[0]), int(cord_1[1])

for ln in lines:
    stabel(ln)
    for x, y in itertools.product(range(x1, x2 + 1), range(y1, y2 + 1)):
        grid[x][y] = action(inst, grid[x][y], 0)

print(sum(itertools.chain(*grid)))

# --- Part Two ---

for ln in lines:
    stabel(ln)
    for x, y in itertools.product(range(x1, x2 + 1), range(y1, y2 + 1)):
        grid[x][y] = action(inst, grid[x][y], 1)

print(sum(itertools.chain(*grid)))
