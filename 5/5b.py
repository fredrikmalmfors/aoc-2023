from collections import defaultdict
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

sweeds = [int(x) for x in lines[0].split()[1:]]

seeds = []
# for i in range(0, len(sweeds), 2):
#     for j in range(sweeds[i], sweeds[i] + sweeds[i + 1], 100000):
#         seeds.append(j)
for x in range(3521000000, 3522000000, 1):
    seeds.append(x)

# print(seeds)


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
# print(prev[106787])
for bb in k:
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
    print(prev[106787])
    print("MIN", min(prev), prev.index(min(prev)))
