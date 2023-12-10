import sys
from collections import defaultdict, Counter
import numpy as np
import math

sys.setrecursionlimit(10000)  # hehe

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

RIGHT = [0, 1]
DOWN = [1, 0]
LEFT = [0, -1]
UP = [-1, 0]

UP_LEFT = [-1, -1]
UP_RIGHT = [-1, 1]
DOWN_LEFT = [1, -1]
DOWN_RIGHT = [1, 1]

DIRS = [RIGHT, DOWN, LEFT, UP]

CHARS = {
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "L": [UP, RIGHT],
    "J": [UP, LEFT],
    "7": [LEFT, DOWN],
    "F": [RIGHT, DOWN],
    ".": [],
}

"""
Find S
Look for connections:
    look_dir == (pipe_dir + 2) % 4
"""


def get_s():
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == "S":
                return (y, x)
    assert False


def oppo_dir(dd):
    return [-1 * x for x in dd]


def pos_by(cc, dd):
    return (cc[0] + dd[0], cc[1] + dd[1])


def get_char(pos):
    return lines[pos[0]][pos[1]]


LL = set()
RR = set()

orien = 0

CLOCK = [("L", LEFT), ("F", UP), ("7", RIGHT), ("J", DOWN)]
COUNT = [("F", LEFT), ("L", DOWN), ("J", RIGHT), ("7", UP)]

stack = []
cc = get_s()
prev = None
done = False
while not done:
    nex = None
    cc_char = get_char(cc)
    if cc_char == "S":
        for dd in DIRS:
            lp = pos_by(cc, dd)
            hoo = CHARS[get_char(lp)]
            if oppo_dir(dd) in hoo:
                nex = lp
                break
    else:
        for dd in CHARS[cc_char]:
            lp = pos_by(cc, dd)
            if prev and lp == prev:
                continue
            lp_char = get_char(lp)
            if lp_char == "S":
                done = True
                break
            hoo = CHARS[lp_char]
            if oppo_dir(dd) in hoo:
                # dd lp_char
                if (lp_char, dd) in CLOCK:
                    orien += 1
                if (lp_char, dd) in COUNT:
                    orien -= 1
                nex = lp
                break
    prev = cc
    cc = nex

    """
    x x x
    x F -
    x | x
    
    """

    ####
    try:
        kk = get_char(cc)

    except:
        stack.append(cc)
        break
    if kk == "-":
        RR.add(pos_by(cc, UP if prev == pos_by(cc, RIGHT) else DOWN))
        LL.add(pos_by(cc, DOWN if prev == pos_by(cc, RIGHT) else UP))
    if kk == "|":
        RR.add(pos_by(cc, RIGHT if prev == pos_by(cc, DOWN) else LEFT))
        LL.add(pos_by(cc, DOWN if prev == pos_by(cc, DOWN) else RIGHT))
    if kk == "F":
        if prev == pos_by(cc, DOWN):
            LL.add(pos_by(cc, LEFT))
            LL.add(pos_by(cc, UP))
            LL.add(pos_by(cc, UP_LEFT))
        elif prev == pos_by(cc, RIGHT):
            RR.add(pos_by(cc, UP))
            RR.add(pos_by(cc, LEFT))
            RR.add(pos_by(cc, UP_LEFT))
    if kk == "7":
        if prev == pos_by(cc, DOWN):
            RR.add(pos_by(cc, RIGHT))
            RR.add(pos_by(cc, UP))
            RR.add(pos_by(cc, UP_RIGHT))
        if prev == pos_by(cc, LEFT):
            LL.add(pos_by(cc, UP))
            LL.add(pos_by(cc, RIGHT))
            LL.add(pos_by(cc, UP_RIGHT))
    if kk == "J":
        if prev == pos_by(cc, UP):
            LL.add(pos_by(cc, RIGHT))
            LL.add(pos_by(cc, DOWN))
            LL.add(pos_by(cc, DOWN_RIGHT))
        if prev == pos_by(cc, LEFT):
            RR.add(pos_by(cc, DOWN))
            RR.add(pos_by(cc, RIGHT))
            RR.add(pos_by(cc, DOWN_RIGHT))
    if kk == "L":
        if prev == pos_by(cc, UP):
            RR.add(pos_by(cc, LEFT))
            RR.add(pos_by(cc, DOWN))
            RR.add(pos_by(cc, DOWN_LEFT))
        if prev == pos_by(cc, DOWN):
            LL.add(pos_by(cc, DOWN))
            LL.add(pos_by(cc, LEFT))
            LL.add(pos_by(cc, DOWN_LEFT))

    print(cc_char)
    stack.append(cc)
stack[-1] = get_s()
print(stack)
for ss in stack:
    RR.discard(ss)
    LL.discard(ss)

print(RR)
print(LL)
clockwise = bool(orien > 0)


def trev(pos):
    print("pos:", pos)
    for dd in DIRS:
        lp = pos_by(pos, dd)
        if not (0 <= lp[0] < len(lines)):
            continue
        if not (0 <= lp[1] < len(lines[0])):
            continue
        if lp in RR or lp in LL or lp in stack:
            continue
        if pos in RR:
            RR.add(lp)
        if pos in LL:
            LL.add(lp)
        trev(lp)


for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if (y, x) in RR or (y, x) in LL:
            print("-->", (y, x))
            trev((y, x))

print(len(RR), RR)
print(len(LL), LL)
print(clockwise)

ans = len(RR) if clockwise else len(LL)


print("---------------")
for y, line in enumerate(lines):
    topri = ""
    for x, ch in enumerate(line):
        if (y, x) in RR:
            topri += "O"
        elif (y, x) in LL:
            topri += "I"
        else:
            topri += "."
    print(topri)

print("\nans:", ans)
