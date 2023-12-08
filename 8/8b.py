import sys
from collections import defaultdict, Counter
import numpy as np
import math

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

inst, rest = lines[0], lines[2:]

M = {}

for ll in rest:
    a, b = ll.split(" = ")
    M[a] = [b[1:4], b[6:9]]

HAM = {}

for cod in M.keys():
    if cod[2] == "A":
        steps = 0
        curr = cod
        offset = 0
        period = 0
        while True:
            loc = inst[steps % len(inst)]
            curr = M[curr][0] if loc == "L" else M[curr][1]
            steps += 1
            if curr[2] == "Z":
                if not offset:
                    offset = steps
                elif not period:
                    period = steps - offset
                else:
                    assert steps == period * 2 + offset
                    break
        print(cod, offset, period)
        HAM[cod] = (offset, period)

# From the largest offset, take large step
argmax_p = max(HAM, key=lambda x: HAM[x][1])

steps, PER = HAM[argmax_p]
per_count = 0
while True:
    he = [
        pp
        for oo, pp in HAM.values()
        if ((steps - oo) / pp) == math.floor((steps - oo) / pp)
    ]

    # lcd = a * b / gcd()

    # gcd =

    if he:
        nev = math.lcm(*he)
        if nev > PER:
            PER = nev
            print(PER)
    # print(steps, he)
    if len(he) == len(HAM.keys()):
        print(steps)
        break
    steps += PER
