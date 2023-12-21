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

HAKI = 9 * 4 * len(lines) * len(lines[0])

cc = 0
while Q:
    Q = deque(sorted(Q, key=lambda x: x[3]))

    pos, aim, count, score = Q.popleft()
    # print("\n", pos, aim, count, score)
    y, x = pos
    dizval = MAP[pos]

    # Add to memory
    prev = M[(pos, aim, count)]
    nev = score + dizval

    if nev >= prev:
        continue

    M[(pos, aim, count)] = nev

    if count < 4:
        ok = [0]
    elif 4 <= count < 10:
        ok = [-1, 0, 1]
    else:
        ok = [-1, 1]

    # print("-----------------", count, ok)
    for rot in ok:
        n_aim = (aim + rot) % 4
        dirr = DIRS[n_aim]
        dy, dx = dirr
        ny, nx = y + dy, x + dx
        # print("-->", (y, x), (ny, nx))
        if (ny, nx) not in MAP:
            # print("....")
            continue
        if rot == 0:
            nc = count + 1
        else:
            nc = 1
        neyvor = ((ny, nx), n_aim, nc, score + dizval)
        # print("APP")
        Q.append(neyvor)

    cc += 1
    if cc % 10_000 == 0:
        a = len(M)
        b = HAKI
        print(a * 100 / b, "%", len(Q))


print(min(v for x, v in M.items() if x[0] == goal))
