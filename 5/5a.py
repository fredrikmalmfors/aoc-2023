from collections import defaultdict
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

seeds = [int(x) for x in lines[0].split()[1:]]

i = 1
k: list[list] = []
rea = False
while i < len(lines):
    if lines[i] == "":
        k.append([])
        i += 2
    else:
        k[-1].append([int(x) for x in lines[i].split()])
        i += 1

prev = seeds
for bb in k:
    # mm = {}

    # # Create map
    # for cc in bb:
    #     a, b, c = cc
    #     for i in range(c):
    #         assert b + i not in mm
    #         mm[b + i] = a + i

    nn = []
    for x in prev:
        damat = x
        for cc in bb:
            a, b, c = cc
            if b <= x < b + c:
                damat = x - b + a
                break
        nn.append(damat)

    prev = nn
    # print(prev)

    # # print(prev)
    # prev = [mm[x] if x in mm else x for x in prev]
    print(min(prev))
