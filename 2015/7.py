# --- Day 7: Some Assembly Required ---

import operator as op, functools

Insts = [l.split() for l in (ln for ln in open(0).readlines())]
OPS = {"AND": op.and_, "OR": op.or_, "LSHIFT": op.lshift, "RSHIFT": op.rshift, "NOT": op.inv, "X": lambda x: x}

wires = {}
for inst in Insts:
    match inst:
        case r, "->", w:
            wires[w] = OPS["X"], r
        case *l, opr, r, "->", w:
            wires[w] = OPS[opr], *l, r

@functools.cache
def solve(w):
    if isinstance(w, int) or w[0].isdigit():
        return int(w) & 0xffff
    return wires[w][0](*[solve(arg) for arg in wires[w][1:]]) & 0xffff

print(p1 := solve("a"))
solve.cache_clear()

# --- Part Two ---

wires["b"] = (OPS["X"], p1)
print(solve("a"))
