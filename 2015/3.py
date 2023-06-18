# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

poles = [pole for pole in input()]
gifted : set = set()
x, y = 0, 0
gifted.add((x, y))

for pole in poles:
    if pole == '^':
        y += 1
    elif pole == 'v':
        y -= 1
    elif pole == '<':
        x -= 1
    elif pole  == '>':
        x += 1

    gifted.add((x, y))

print(len(gifted))

# --- Part Two ---

gifted = set()

robo = False
x1, y1 = 0, 0
x2, y2 = 0, 0

x,  y  = 0, 0
gifted.add((x, y))

for pole in poles:
    if pole == '^':
        if robo:
            y2 += 1
        else:
            y1 += 1
    elif pole == 'v':
        if robo:
            y2 -= 1
        else:
            y1 -= 1
    elif pole == '<':
        if robo:
            x2 -= 1
        else:
            x1 -= 1
    elif pole  == '>':
        if robo:
            x2 += 1
        else:
            x1 += 1

    if robo:
        x, y = x2, y2
    else:
        x, y = x1, y1

    gifted.add((x, y))
    robo = not robo

print(len(gifted))
