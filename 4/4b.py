from collections import defaultdict
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

Q = {k: 1 for k in range(len(lines))}
MEM = {}


for i, ll in enumerate(lines):
    a, b = ll.split(": ")
    b, c = b.split(" | ")
    b = [x for x in b.split(" ") if x]
    c = [x for x in c.split(" ") if x]

    haha = len(set.intersection(set(b), set(c)))
    MEM[i] = haha

for k, coun in Q.items():
    val = MEM[k]
    for ez in range(val):
        Q[k + ez + 1] += coun


print(sum(Q.values()))
