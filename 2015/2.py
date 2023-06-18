# --- Day 2: I Was Told There Would Be No Math ---

lines = open(0).read().splitlines()

def total_area(l : int, w : int, h : int) -> int:
    return 2*(l*w + w*h + h*l) + (l * w)

sf_of_paper = 0

for ln in lines:
    l, w, h = sorted([int(n) for n in ln.split("x")])
    sf_of_paper += total_area(l,w,h)

print(sf_of_paper)

# --- Part Two ---

f_ribbon = 0

for ln in lines:
    l, w, h = sorted([int(n) for n in ln.split("x")])
    f_ribbon += (2 * (l + w)) + (l * w * h)
            
print(f_ribbon)
