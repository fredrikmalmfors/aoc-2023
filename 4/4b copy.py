from collections import defaultdict
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

Q = list(range(len(lines)))
C = defaultdict(int)
MEM = {}


def heik(i):
    global MEM

    if i in MEM:
        return MEM[i]

    ll = lines[i]
    a, b = ll.split(": ")
    b, c = b.split(" | ")
    b = [x for x in b.split(" ") if x]
    c = [x for x in c.split(" ") if x]

    haha = len(set.intersection(set(b), set(c)))
    MEM[i] = haha
    return haha


while Q:
    i = Q.pop(0)
    C[i] += 1
    print(i, len(Q))

    haha = heik(i)

    if haha > 0:
        Q.extend(list(range(i + 1, i + haha + 1)))
        Q.sort()

print(sum(C.values()))
