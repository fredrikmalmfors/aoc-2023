import sys
from collections import defaultdict, Counter
import numpy as np
import math

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

RIGHT = [0, 1]
DOWN = [1, 0]
LEFT = [0, -1]
UP = [-1, 0]

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


stack = []
cc = get_s()
prev = None
while True:
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
                print("YOO")
                print(stack)
                print(len(stack))
                print(math.ceil(len(stack) / 2))
                sys.exit()
            hoo = CHARS[lp_char]
            if oppo_dir(dd) in hoo:
                nex = lp
                break
    prev = cc
    cc = nex
    print(cc_char)
    stack.append(cc)
