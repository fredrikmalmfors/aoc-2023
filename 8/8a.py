import sys
from collections import defaultdict, Counter
import numpy as np

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

inst, rest = lines[0], lines[2:]

M = {}

for ll in rest:
    a, b = ll.split(" = ")
    M[a] = [b[1:4], b[6:9]]

steps = 0
curr = "AAA"
while True:
    loc = inst[steps % len(inst)]
    curr = M[curr][0] if loc == "L" else M[curr][1]
    steps += 1
    if curr == "ZZZ":
        print(steps)
        break

# print(M)
