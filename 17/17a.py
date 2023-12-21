from collections import defaultdict, deque
from copy import copy
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
MAP = {(y, x): int(val) for y, row in enumerate(lines) for x, val in enumerate(row)}

goal = (len(lines) - 1, len(lines[0]) - 1)

M = defaultdict(lambda: float("inf"))
Q = deque([((0, 1), 0, 1, 0), ((1, 0), 1, 1, 0)])

HAKI = 3 * 4 * len(lines) * len(lines[0])

cc = 0
while Q:
    Q = deque(sorted(Q, key=lambda x: x[3]))

    pos, aim, count, score = Q.popleft()
    y, x = pos
    dizval = MAP[pos]

    # Add to memory
    prev = M[(pos, aim, count)]
    nev = score + dizval

    if nev >= prev:
        continue

    M[(pos, aim, count)] = nev

    # look around
    for n_aim, (dy, dx) in enumerate(DIRS):
        if abs(aim - n_aim) == 2:
            continue
        ny, nx = y + dy, x + dx
        if (ny, nx) not in MAP:
            continue
        if aim == n_aim:
            if count == 3:
                continue
            nc = count + 1
        else:
            nc = 1
        neyvor = ((ny, nx), n_aim, nc, score + dizval)
        Q.append(neyvor)

    cc += 1
    if cc % 10_000 == 0:
        print(len(M), "/", HAKI, "--", len(Q))


print(min(v for x, v in M.items() if x[0] == goal))
